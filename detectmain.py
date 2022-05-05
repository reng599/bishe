#import os
#import subprocess
import sys

#import cv2
from PyQt5.QtCore import QTimer, QCoreApplication
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame,QInputDialog,QFileDialog,QMessageBox
from newwindow import *
import winsound
import threading
from ThreadCapturecall import ThreadCapture
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from database import *
import datetime



class mWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(mWindow, self).__init__()
        self.setupUi(self)

        self.mailbutton.clicked.connect(self.setmail)
        self.sirenbutton.clicked.connect(self.setsiren)
        self.sirenon = False 
        self.mailon = False
        self.usermail = ''
        self.username = ''
        #self.password = ''
        self.filePath = '0'
        self.checkfps = False
        self.checkskeleton = False
        self.checkprobability = False
        self.checknormality = False

        self.predictbutton.clicked.connect(self.switchdectect)
        self.selectvideo.clicked.connect(self.clickselectvideo)
        self.camerabutton.clicked.connect(self.clickcamerabtn)
        self.checkfpsbtn.clicked.connect(self.clickfps)
        self.checkskeletonbtn.clicked.connect(self.clickskeleton)
        self.checkprobabilitybtn.clicked.connect(self.clickprobability)
        self.checknormalitybtn.clicked.connect(self.clicknormality)
        self.newpwdbtn.clicked.connect(self.updatepwd)
        self.newmailbtn.clicked.connect(self.updatemail)
        self.newphonebtn.clicked.connect(self.updatephone)
        self.searchinfobtn.clicked.connect(self.displayinfo)
        self.conn = None


        # ================ 关闭窗口的美化 =========================
        # self.pushButton_5.setFixedSize(15, 15)
        # self.pushButton_6.setFixedSize(15, 15)
        # self.pushButton_7.setFixedSize(15, 15)
        # self.pushButton_5.setStyleSheet(
        #     '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
        # self.pushButton_6.setStyleSheet(
        #     '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        # self.pushButton_7.setStyleSheet(
        #     '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        # self.pushButton_7.clicked.connect(QCoreApplication.instance().quit)
        #self.setWindowFlag(QtCore.Qt.FramelessWindowHint)


    def preset(self,mail_address,username,conn):
        self.usermail = mail_address
        self.username = username
        self.conn = conn

    def clickfps(self):
        self.checkfps = not self.checkfps
    def clickskeleton(self):
        self.checkskeleton = not self.checkskeleton
    def clickprobability(self):
        self.checkprobability = not self.checkprobability
    def clicknormality(self):
        self.checknormality = not self.checknormality

    def updatemail(self):
        newmail = self.newmail_le.text()
        import re
        ex_email = re.compile(r'^[a-z0-9. %+-]+@[a-z0-9.-]+\.[a-z]{2,4}$')
        if ex_email.match(newmail):
            res = dbupdatemail(self.username,newmail,self.conn)
            if res:
                QMessageBox.about(self,"成功","邮箱已更改")
            else:
                QMessageBox.about(self,"失败","请重试")
        else:
            QMessageBox.about(self,"不合法","请重新输入邮箱")

    def updatephone(self):
        newphone = self.newphone_le.text()
        import re
        ex_phone = re.compile(r'1[3,4,5,7,8]\d{9}')
        if ex_phone.match(newphone):
            res = dbupdatephone(self.username,newmail,self.conn)
            if res:
                QMessageBox.about(self,"成功","手机号已更改")
            else:
                QMessageBox.about(self,"失败","请重试")
        else:
            QMessageBox.about(self,"不合法","请重新输入手机号")

    def updatepwd(self):
        newpwd = self.newpwd_le.text()
        res = dbupdatepwd(self.username,newpwd,self.conn)
        if res:
            QMessageBox.about(self,"成功","密码已更改")
        else:
            QMessageBox.about(self,"失败","请重试")

    def displayinfo(self):
        record_list = dbsearchinfo(self.username,self.conn)
        if record_list:
            self.textBrowser.clear()
            for record in record_list:
                falltime = record[1].strftime('%Y-%m-%d %H:%M:%S')
                fromcamera = " 来源于摄像头监测" if record[2] else " 来源于已有视频检测"
                emailed = ",已发送邮件提醒" if record[3] else ",未设置邮件提醒"
                self.textBrowser.append("时间："+falltime+fromcamera+emailed+'\n')

        else:
            self.textBrowser.append("无摔倒记录！")


    def setmail(self):
        use_presetmail = QMessageBox.question(self,"邮箱？","是否使用注册邮箱",QMessageBox.Yes | QMessageBox.No)
        if use_presetmail == QMessageBox.No:
            user,ok = QInputDialog.getText(self, '邮箱', '请输入您的邮箱：')
            if  user and ok:
                self.usermail = user
                self.mailbutton.setText('已设邮箱')
                print('new mail:'+user)
        elif use_presetmail == QMessageBox.Yes:
            self.mailbutton.setText('已设邮箱')
        self.mailon = True



    def setsiren(self):
        if self.sirenon:
            self.sirenbutton.setText('设置警报')
        else:
            self.sirenbutton.setText('已设警报')
        self.sirenon = not self.sirenon


    def switchdectect(self):
        if self.predictbutton.text() == '点击开始':              
                self.threadCapture = ThreadCapture(self.filePath,self.checknormality,self.checkprobability,self.checkskeleton,self.checkfps)
                self.threadCapture.signal_image.connect(self.showImage)
                self.threadCapture.start()
                self.predictbutton.setText('点击结束')

                
        else:
            #self.threadCapture.releasecam()
            #print('before terminate')
            self.threadCapture.terminate()
            #print('after terminate')
            self.threadCapture.quit()
            #print('after quit')
            #self.threadCapture.releasecam()
            self.predictbutton.setText('点击开始')



    def clickselectvideo(self):
        if self.videobutton.isChecked():
            self.filePath, _ = QFileDialog.getOpenFileName(self, caption="选取视频", filter="*.mp4")
            print(self.filePath)
            self.selectvideo.setText('视频已选择')
        else:
            QMessageBox.about(self,"提示","请先点击检测视频按钮")


    def clickcamerabtn(self):
        if self.filePath:
            self.filePath = '0'
            self.selectvideo.setText('选择视频')


    def showImage(self,image):
        self.label_3.setPixmap(image)
        self.label_7.setPixmap(QtGui.QPixmap("sundry/info.png"))
        self.label_8.setText('异常！')

        #self.label_3.setScaledContents (True)
        if self.sirenon:
            threading.Thread(target=winsound.Beep,args=[1000,2000]).start()
        if self.mailon:            
            smtp_server = 'smtp.qq.com'
            msg = MIMEText('系统刚刚监测到老人可能发生摔倒，请及时确认','plain','utf-8')
            msg['From'] = Header('家庭智能监控系统')
            msg['To'] = Header('监控系统用户')
            msg['Subject'] = Header('家中老人可能发生摔倒！')

            try:
                server = smtplib.SMTP_SSL(smtp_server)
                server.connect(smtp_server,465)

                server.login('964686404@qq.com','evuokpfkkpekbeed')

                server.sendmail('964686404@qq.com', self.usermail, msg.as_string())
            except smtplib.SMTPException as e:
                print('email sent failed '+str(e))
            finally:
                server.quit()

        curr_time = datetime.datetime.now()
        time_str = curr_time.strftime('%Y-%m-%d %H:%M:%S')
        dbinsertinfo(self.username,time_str,self.filePath,self.mailon,self.conn)

    def closeEvent(self,event):
        dbclose(self.conn)
        event.accept()
        sys.exit(0) 


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywin = mWindow()
    mywin.setStyleSheet("#MainWindow{border-image:url(sundry/back5.png);}")
    mywin.show()
    sys.exit(app.exec_())
