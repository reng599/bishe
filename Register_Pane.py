from PyQt5.Qt import *
from resource.register import Ui_Form


class RegisterPane(QWidget, Ui_Form):
    exit_signal = pyqtSignal()
    register_account_pwd_signal = pyqtSignal(str,str,str,str)

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)

        self.animation_targets=[self.about_menu_btn,self.reset_menu_btn,self.exit_menu_btn]
        self.animation_targets_pos = [target.pos() for target in self.animation_targets]

    def show_hide_menu(self,checked):
        print("显示和隐藏",checked)

        animation_group = QSequentialAnimationGroup(self)
        for idx,target in enumerate(self.animation_targets):
            animation = QPropertyAnimation()
            animation.setTargetObject(target)
            animation.setPropertyName(b"pos")
            animation.setStartValue(self.main_menu_btn.pos())
            animation.setEndValue(self.animation_targets_pos[idx])
            animation.setDuration(100)
            animation.setEasingCurve(QEasingCurve.OutBounce)
            animation_group.addAnimation(animation)
        if not checked:
            animation_group.setDirection(QAbstractAnimation.Forward)
        else:
            animation_group.setDirection(QAbstractAnimation.Backward)
        animation_group.start(QAbstractAnimation.DeleteWhenStopped)

    def show_about_menu(self):
        print("关于")
        QMessageBox.about(self, "家庭智慧监控系统","2018级软件工程任鹏飞")

    def show_reset_menu(self):
        print("清空")
        self.account_le.clear()
        self.password_le.clear()
        self.confirm_pwd_le.clear()
        self.mail_le.clear()

    def show_exit_menu(self):
        self.exit_signal.emit()

    def register(self):
        account_txt = self.account_le.text()
        password_txt = self.password_le.text()
        phone_txt = self.confirm_pwd_le.text()
        mail_txt = self.mail_le.text()
        self.register_account_pwd_signal.emit(account_txt,password_txt,phone_txt,mail_txt)

    def enable_register_btn(self):
        account_txt = self.account_le.text()
        password_txt = self.password_le.text()
        phone = self.confirm_pwd_le.text()
        mail = self.mail_le.text()
        if len(account_txt)>0 and len(password_txt)>0 and len(phone)>0 and len(mail):
            self.register_btn.setEnabled(True)
        else:
            self.register_btn.setEnabled(False)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = RegisterPane()
    window.exit_signal.connect(lambda :print("退出"))
    window.register_account_pwd_signal.connect(lambda sig1,sig2:print(sig1,sig2))
    window.show()
    sys.exit(app.exec_())
