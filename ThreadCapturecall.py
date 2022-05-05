import cv2
from PyQt5.QtCore import QThread, pyqtSignal#, QMutex
from PyQt5.QtGui import QImage, QPixmap

import os
import time
import torch
import numpy as np

from Detection.Utils import ResizePadding
from CameraLoader import CamLoader, CamLoader_Q
from DetectorLoader import TinyYOLOv3_onecls

from PoseEstimateLoader import SPPE_FastPose
from fn import draw_single

from Track.Tracker import Detection, Tracker
from ActionsEstLoader import TSSTG


def preproc(image):
    """preprocess function for CameraLoader.
    """
    resize_fn = ResizePadding(384,384)
    image = resize_fn(image)

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image


def kpt2bbox(kpt, ex=20):
    """Get bbox that hold on all of the keypoints (x,y)
    kpt: array of shape `(N, 2)`,
    ex: (int) expand bounding box,
    """
    return np.array((kpt[:, 0].min() - ex, kpt[:, 1].min() - ex,
                     kpt[:, 0].max() + ex, kpt[:, 1].max() + ex))



class ThreadCapture(QThread):
    # 定义信号，用于传输图像
    signal_image = pyqtSignal(QPixmap)
    #signal_threaddone = pyqtSignal(bool)
    def __init__(self,camera,normality,probability,skeleton,fps):#cameraNum
        super(ThreadCapture, self).__init__()
        #self.cameraNum = cameraNum
        #self.qmutex = QMutex()  # 进行锁
        self.displayprobability = probability
        self.displayskeleton = skeleton
        self.displayfps = fps
        self.displaynormality = normality
        self.cam_source = camera
        self.cam = None
        self.stop = False
        print('this is a new run for '+camera)


    def run(self):

        #os.system('python main.py -C 0')
        #operation(camera='0')
    

        # DETECTION MODEL.
        inp_dets = 384
        detect_model = TinyYOLOv3_onecls(inp_dets, device='cuda')

        # POSE MODEL.
        pose_model = SPPE_FastPose('resnet50', 224, 160, device='cuda')

        # Tracker.
        max_age = 30
        tracker = Tracker(max_age=max_age, n_init=3)

        # Actions Estimate.
        action_model = TSSTG()

        #resize_fn = ResizePadding(inp_dets, inp_dets)

        cam_source = self.cam_source
        if type(cam_source) is str and os.path.isfile(cam_source):
            # Use loader thread with Q for video file.
            self.cam = CamLoader_Q(cam_source, queue_size=1000, preprocess=preproc).start()
        else:
            # Use normal thread loader for webcam.
            self.cam = CamLoader(int(cam_source) if cam_source.isdigit() else cam_source,
                            preprocess=preproc).start()


        print('have a camera for'+cam_source)
        fps_time = 0
        last_fall_time = 0
        first_fall = True
        f = 0
        while self.cam.grabbed():
            f += 1
            frame = self.cam.getitem()
            # print('cam is on,img size is')
            # print(frame.shape)
            #image = frame.copy()
            action_name = ''

            # Detect humans bbox in the frame with detector model.
            detected = detect_model.detect(frame, need_resize=False, expand_bb=10)

            # Predict each tracks bbox of current frame from previous frames information with Kalman filter.
            tracker.predict()
            # Merge two source of predicted bbox together.
            for track in tracker.tracks:
                det = torch.tensor([track.to_tlbr().tolist() + [0.5, 1.0, 0.0]], dtype=torch.float32)
                detected = torch.cat([detected, det], dim=0) if detected is not None else det

            detections = []  # List of Detections object for tracking.
            if detected is not None:
                #detected = non_max_suppression(detected[None, :], 0.45, 0.2)[0]
                # Predict skeleton pose of each bboxs.
                poses = pose_model.predict(frame, detected[:, 0:4], detected[:, 4])

                # Create Detections object.
                detections = [Detection(kpt2bbox(ps['keypoints'].numpy()),
                                        np.concatenate((ps['keypoints'].numpy(),
                                                        ps['kp_score'].numpy()), axis=1),
                                        ps['kp_score'].mean().numpy()) for ps in poses]


            # Update tracks by matching each track information of current and previous frame or
            # create a new track if no matched.
            tracker.update(detections)

            # Predict Actions of each track.
            for i, track in enumerate(tracker.tracks):
                if not track.is_confirmed():
                    continue

                track_id = track.track_id
                bbox = track.to_tlbr().astype(int)
                center = track.get_center().astype(int)

                action = 'pending..'
                clr = (0, 255, 0)
                # Use 30 frames time-steps to prediction.
                if len(track.keypoints_list) == 30:
                    pts = np.array(track.keypoints_list, dtype=np.float32)
                    out = action_model.predict(pts, frame.shape[:2])
                    action_name = action_model.class_names[out[0].argmax()]
                    if self.displayprobability:
                        action = '{}: {:.2f}%'.format(action_name, out[0].max() * 100)
                    else:
                        action = action_name
                    if action_name == 'Fall Down':
                        clr = (255, 0, 0)
                        fall_time = time.time()
                        if first_fall or fall_time - last_fall_time >= 10:
                            pixmap = self.imageCv2Qt(frame)
                            self.signal_image.emit(pixmap)
                            last_fall_time = fall_time
                            first_fall = False

                    
                    elif action_name == 'Lying Down':
                        clr = (255, 200, 0)
                        fall_time = time.time()
                        if first_fall or fall_time - last_fall_time >= 10:
                            pixmap = self.imageCv2Qt(frame)
                            self.signal_image.emit(pixmap)
                            last_fall_time = fall_time
                            first_fall = False
                        


                # VISUALIZE.
                if track.time_since_update == 0:
                    if self.displayskeleton:
                        frame = draw_single(frame, track.keypoints_list[-1])
                    frame = cv2.rectangle(frame, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (0, 255, 0), 1)
                    frame = cv2.putText(frame, str(track_id), (center[0], center[1]), cv2.FONT_HERSHEY_COMPLEX,
                                        0.4, (255, 0, 0), 2)
                    if self.displaynormality or action_name == 'Fall Down' or action_name == 'Lying Down':
                        frame = cv2.putText(frame, action, (bbox[0] + 5, bbox[1] + 15), cv2.FONT_HERSHEY_COMPLEX,
                                          0.4, clr, 1)


            # Show Frame.
            frame = cv2.resize(frame, (0, 0), fx=2., fy=2.)

            if self.displayfps:
                frame = cv2.putText(frame, '%d, FPS: %f' % (f, 1.0 / (time.time() - fps_time)),
                                    (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

            frame = frame[:, :, ::-1]
            fps_time = time.time()


            cv2.imshow('frame', frame)
            # print('after 174 cv2.resize,img size is ')
            # print(frame.shape)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print('q pressed')
                self.cam.stop()
                cv2.destroyAllWindows()

        # Clear resource.
        self.cam.stop()
        print('1\n')
        # if outvid:
        #     writer.release()
        cv2.destroyAllWindows()
        print('cv2 destroyed')
        #self.signal_threaddone.emit(True)


    def releasecam(self):
        self.cam.stop()
        #cv2.destroyAllWindows()
        #print('2\n')

    def __del__(self):
        #print('3\n')
        self.cam.stop()
        #cv2.destroyAllWindows()
        

    def __exit__(self, exc_type, exc_val, exc_tb):
        #print('4\n')
        self.cam.stop()
        



    # 转换为qt的图像格式
    def imageCv2Qt(self, rgb):
        #rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width, depth = rgb.shape
        bytesPerLine = width * depth
        qrgb = QImage(rgb.data, width, height, bytesPerLine, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qrgb)
        return pixmap

