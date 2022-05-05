
from Login_Pane import LoginPane
from Register_Pane import RegisterPane
#from Calculate_Pane import CalculatePane
from PyQt5.Qt import *
from detectmain import mWindow
import pymssql
from database import *
from sendmessage import Sample

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)



    # 控件面板的创建
    login_pane = LoginPane()
    register_pane = RegisterPane(login_pane)
    register_pane.move(0, login_pane.height())
    register_pane.show()
    #calculator_pane = CalculatePane()
    mywin = mWindow()
    mywin.setStyleSheet("#MainWindow{border-image:url(sundry/back5.png);}")
    # conn = pymssql.connect('LAPTOP-ORS00ARI', 'sa', '123', 'EDUC')
    # cursor = conn.cursor()
    conn = dbinit()

    # 槽函数
    def exit_register_pane():
        animation = QPropertyAnimation(register_pane)
        animation.setTargetObject(register_pane)
        animation.setPropertyName(b"pos")
        animation.setStartValue(QPoint(0, 0))
        animation.setEndValue(QPoint(login_pane.width(), 0))
        animation.setDuration(500)
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    def show_register_pane():
        animation = QPropertyAnimation(register_pane)
        animation.setTargetObject(register_pane)
        animation.setPropertyName(b"pos")
        animation.setStartValue(QPoint(0, login_pane.height()))
        animation.setEndValue(QPoint(0,0))
        animation.setDuration(500)
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    def check_login(account,pwd):
        res = dbsearch(account,conn)
        if res:
            if res[1].strip() == pwd:
                mywin.preset(res[3].strip(),res[0].strip(),conn)
                mywin.show()
                login_pane.hide()
                #dbclose(conn)
            else:
                login_pane.show_error_animation()
                reply = QMessageBox.question(login_pane,"找回？","是否要找回密码",QMessageBox.Yes | QMessageBox.No)
                if reply == QMessageBox.Yes:
                    phone,ok = QInputDialog.getText(login_pane, '手机号', '请输入注册手机号：')
                    if phone and ok and res[2].strip() == phone:
                        Sample.main(phone,res[1].strip())
                        QMessageBox.about(login_pane,"提示","已给手机发送密码短信")

        else:
                login_pane.show_error_animation()
                QMessageBox.about(login_pane,"无账户","请先注册账户")      


    def check_register(account,pwd,phone,mail):
        res = dbsearch(account,conn)
        if not res:
            import re
            ex_email = re.compile(r'^[a-z0-9. %+-]+@[a-z0-9.-]+\.[a-z]{2,4}$')
            ex_phone = re.compile(r'1[3,4,5,7,8]\d{9}')
            if ex_email.match(mail):
                if ex_phone.match(phone):
                    import random
                    validation = random.randint(0,9999)
                    Sample.main(phone,validation)
                    user_input,ok = QInputDialog.getText(login_pane, '提示', '请输入手机收到的验证码：')
                    if ok and user_input == str(validation):
                        saction = dbinsert(account,pwd,phone,mail,conn)
                        if saction:
                            QMessageBox.about(login_pane,"成功","请返回登录")
                        else:
                            QMessageBox.about(login_pane,"失败","请重新尝试")
                else:
                    QMessageBox.about(login_pane,"不合法","请重新输入手机号")

            else:
                QMessageBox.about(login_pane,"不合法","请重新输入邮箱")

        else:
            QMessageBox.about(login_pane,"账号重复","请换一个用户名")



    # 信号的连接
    register_pane.exit_signal.connect(exit_register_pane)
    register_pane.register_account_pwd_signal.connect(check_register)
    login_pane.show_register_pane_signal.connect(show_register_pane)
    login_pane.check_login_signal.connect(check_login)

    login_pane.show()
    sys.exit(app.exec_())

