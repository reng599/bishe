# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\Actionfall\resource\UI\register.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 450)
        Form.setMinimumSize(QtCore.QSize(500, 450))
        Form.setMaximumSize(QtCore.QSize(500, 450))
        Form.setStyleSheet("QWidget#Form{\n"
"    border-image: url(G:/Actionfall/resource/images/bluegb.jfif);\n"
"}")
        self.main_menu_btn = QtWidgets.QPushButton(Form)
        self.main_menu_btn.setGeometry(QtCore.QRect(20, 20, 50, 50))
        self.main_menu_btn.setStyleSheet("QPushButton{\n"
"    border-radius:25px;\n"
"    background-color: white;\n"
"    color:rgb(32, 41, 71)\n"
"}\n"
"QPushButton:hover{\n"
"    border: 4px solid white;\n"
"    background-color: black;\n"
"    color:white;\n"
"}\n"
"QPushButton:checked{\n"
"    border: 2px solid white;\n"
"    background-color: black;\n"
"    color:white;\n"
"}")
        self.main_menu_btn.setCheckable(True)
        self.main_menu_btn.setObjectName("main_menu_btn")
        self.exit_menu_btn = QtWidgets.QPushButton(Form)
        self.exit_menu_btn.setGeometry(QtCore.QRect(20, 110, 50, 50))
        self.exit_menu_btn.setStyleSheet("QPushButton{\n"
"    border-radius:25px;\n"
"    background-color: white;\n"
"    color:rgb(32, 41, 71)\n"
"}\n"
"QPushButton:hover{\n"
"    border: 4px solid white;\n"
"    background-color: black;\n"
"    color:white;\n"
"}\n"
"QPushButton:checked{\n"
"    border: 2px solid white;\n"
"    background-color: black;\n"
"    color:white;\n"
"}")
        self.exit_menu_btn.setCheckable(False)
        self.exit_menu_btn.setObjectName("exit_menu_btn")
        self.reset_menu_btn = QtWidgets.QPushButton(Form)
        self.reset_menu_btn.setGeometry(QtCore.QRect(110, 90, 50, 50))
        self.reset_menu_btn.setStyleSheet("QPushButton{\n"
"    border-radius:25px;\n"
"    background-color: white;\n"
"    color:rgb(32, 41, 71)\n"
"}\n"
"QPushButton:hover{\n"
"    border: 4px solid white;\n"
"    background-color: black;\n"
"    color:white;\n"
"}\n"
"QPushButton:checked{\n"
"    border: 2px solid white;\n"
"    background-color: black;\n"
"    color:white;\n"
"}")
        self.reset_menu_btn.setCheckable(False)
        self.reset_menu_btn.setObjectName("reset_menu_btn")
        self.about_menu_btn = QtWidgets.QPushButton(Form)
        self.about_menu_btn.setGeometry(QtCore.QRect(130, 20, 50, 50))
        self.about_menu_btn.setStyleSheet("QPushButton{\n"
"    border-radius:25px;\n"
"    background-color: white;\n"
"    color:rgb(32, 41, 71)\n"
"}\n"
"QPushButton:hover{\n"
"    border: 4px solid white;\n"
"    background-color: black;\n"
"    color:white;\n"
"}\n"
"QPushButton:checked{\n"
"    border: 2px solid white;\n"
"    background-color: black;\n"
"    color:white;\n"
"}")
        self.about_menu_btn.setCheckable(False)
        self.about_menu_btn.setObjectName("about_menu_btn")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 220, 370, 190))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setStyleSheet("color:black;\n"
"font: 18pt \"Wawati SC\";")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.account_le = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.account_le.sizePolicy().hasHeightForWidth())
        self.account_le.setSizePolicy(sizePolicy)
        self.account_le.setMinimumSize(QtCore.QSize(150, 30))
        self.account_le.setMaximumSize(QtCore.QSize(150, 16777215))
        self.account_le.setStyleSheet("background-color: transparent;\n"
"color:black;\n"
"border:none;\n"
"border-bottom:1px solid white;")
        self.account_le.setText("")
        self.account_le.setFrame(True)
        self.account_le.setClearButtonEnabled(True)
        self.account_le.setObjectName("account_le")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.account_le)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setStyleSheet("color:black;\n"
"font: 18pt \"Wawati SC\";")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.password_le = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password_le.sizePolicy().hasHeightForWidth())
        self.password_le.setSizePolicy(sizePolicy)
        self.password_le.setMinimumSize(QtCore.QSize(150, 30))
        self.password_le.setMaximumSize(QtCore.QSize(150, 16777215))
        self.password_le.setStyleSheet("background-color: transparent;\n"
"color:black;\n"
"border:none;\n"
"border-bottom:1px solid white;")
        self.password_le.setFrame(True)
        self.password_le.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_le.setClearButtonEnabled(True)
        self.password_le.setObjectName("password_le")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.password_le)
        self.confirm_pwd_le = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.confirm_pwd_le.sizePolicy().hasHeightForWidth())
        self.confirm_pwd_le.setSizePolicy(sizePolicy)
        self.confirm_pwd_le.setMinimumSize(QtCore.QSize(150, 30))
        self.confirm_pwd_le.setMaximumSize(QtCore.QSize(150, 16777215))
        self.confirm_pwd_le.setStyleSheet("background-color: transparent;\n"
"color:black;\n"
"border:none;\n"
"border-bottom:1px solid white;")
        self.confirm_pwd_le.setText("")
        self.confirm_pwd_le.setFrame(True)
        self.confirm_pwd_le.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.confirm_pwd_le.setClearButtonEnabled(True)
        self.confirm_pwd_le.setObjectName("confirm_pwd_le")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.confirm_pwd_le)
        self.register_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.register_btn.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.register_btn.sizePolicy().hasHeightForWidth())
        self.register_btn.setSizePolicy(sizePolicy)
        self.register_btn.setMinimumSize(QtCore.QSize(210, 40))
        self.register_btn.setMaximumSize(QtCore.QSize(210, 40))
        self.register_btn.setStyleSheet("QPushButton:disabled{    \n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(82, 81, 83);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton{    \n"
"    background-color: rgb(0,0,0);\n"
"    color: rgb(255,255,255);\n"
"    border-radius: 10px;\n"
"    border: 2px solid white;\n"
"}\n"
"QPushButton:hover{            \n"
"    background-color: rgb(217, 215, 220);\n"
"}\n"
"QPushButton:pressed{                        \n"
"    background-color: rgb(192, 232, 255)\n"
"}")
        self.register_btn.setObjectName("register_btn")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.register_btn)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setStyleSheet("color:black;\n"
"font: 18pt \"Wawati SC\";")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setStyleSheet("color:black;\n"
"font: 18pt \"Wawati SC\";")
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.mail_le = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mail_le.sizePolicy().hasHeightForWidth())
        self.mail_le.setSizePolicy(sizePolicy)
        self.mail_le.setMinimumSize(QtCore.QSize(150, 30))
        self.mail_le.setMaximumSize(QtCore.QSize(150, 16777215))
        self.mail_le.setStyleSheet("background-color: transparent;\n"
"color:black;\n"
"border:none;\n"
"border-bottom:1px solid white;")
        self.mail_le.setFrame(True)
        self.mail_le.setClearButtonEnabled(True)
        self.mail_le.setObjectName("mail_le")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.mail_le)
        self.exit_menu_btn.raise_()
        self.reset_menu_btn.raise_()
        self.about_menu_btn.raise_()
        self.layoutWidget.raise_()
        self.main_menu_btn.raise_()

        self.retranslateUi(Form)
        self.main_menu_btn.clicked.connect(Form.show_hide_menu)
        self.about_menu_btn.clicked.connect(Form.show_about_menu)
        self.reset_menu_btn.clicked.connect(Form.show_reset_menu)
        self.exit_menu_btn.clicked.connect(Form.show_exit_menu)
        self.register_btn.clicked.connect(Form.register)
        self.account_le.textChanged['QString'].connect(Form.enable_register_btn)
        self.password_le.textChanged['QString'].connect(Form.enable_register_btn)
        self.confirm_pwd_le.textChanged['QString'].connect(Form.enable_register_btn)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "TTTEED"))
        self.main_menu_btn.setText(_translate("Form", "菜单"))
        self.exit_menu_btn.setText(_translate("Form", "退出"))
        self.reset_menu_btn.setText(_translate("Form", "重置"))
        self.about_menu_btn.setText(_translate("Form", "关于"))
        self.label.setText(_translate("Form", "账      号："))
        self.label_2.setText(_translate("Form", "密      码："))
        self.register_btn.setText(_translate("Form", "注册"))
        self.label_3.setText(_translate("Form", "手      机："))
        self.label_4.setText(_translate("Form", "邮      箱："))
import source_rc
