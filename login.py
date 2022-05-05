# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\Actionfall\resource\UI\login.ui'
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
        Form.setToolTipDuration(-15)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.login_top_bg_label = QtWidgets.QLabel(self.widget)
        self.login_top_bg_label.setEnabled(False)
        self.login_top_bg_label.setText("")
        self.login_top_bg_label.setObjectName("login_top_bg_label")
        self.horizontalLayout_2.addWidget(self.login_top_bg_label)
        self.verticalLayout.addWidget(self.widget)
        self.login_bottom = QtWidgets.QWidget(Form)
        self.login_bottom.setEnabled(True)
        self.login_bottom.setToolTipDuration(-15)
        self.login_bottom.setStyleSheet("")
        self.login_bottom.setObjectName("login_bottom")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.login_bottom)
        self.horizontalLayout.setContentsMargins(20, 0, 20, 20)
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.login_bottom)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        self.widget_3 = QtWidgets.QWidget(self.login_bottom)
        self.widget_3.setStyleSheet("")
        self.widget_3.setObjectName("widget_3")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout.setContentsMargins(20, -1, 20, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.account_cb = QtWidgets.QComboBox(self.widget_3)
        self.account_cb.setMinimumSize(QtCore.QSize(0, 45))
        self.account_cb.setMaximumSize(QtCore.QSize(16777215, 45))
        self.account_cb.setStyleSheet("QComboBox{\n"
"    font-size: 20px;\n"
"    border: none;\n"
"    border-bottom: 1px solid gray;\n"
"    background-color: transparent;\n"
"}\n"
"QComboBox::drop-down {\n"
"    background-color: transparent;\n"
"    width: 60px;height: 40px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: url(:/login/images/down.png);\n"
"    width: 40px;height: 10px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    min-height: 60px;\n"
"}\n"
"QComboBox QAbstractItemView: item {\n"
"    color: lightblue;\n"
"}\n"
"QComboBox: hover{\n"
"    border-bottom: 1px solid black;\n"
"}\n"
"QComboBox: focus \n"
"{\n"
"     border-bottom: 1px solid rgb(18,183,245);\n"
"}")
        self.account_cb.setEditable(True)
        self.account_cb.setIconSize(QtCore.QSize(16, 16))
        self.account_cb.setFrame(True)
        self.account_cb.setObjectName("account_cb")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/login/images/001.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.account_cb.addItem(icon, "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/login/images/002.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.account_cb.addItem(icon1, "")
        self.gridLayout.addWidget(self.account_cb, 0, 0, 1, 2)
        self.login_btn = QtWidgets.QPushButton(self.widget_3)
        self.login_btn.setEnabled(False)
        self.login_btn.setMinimumSize(QtCore.QSize(0, 45))
        self.login_btn.setMaximumSize(QtCore.QSize(16777215, 45))
        self.login_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(33,174,250);\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(72,203,250);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(85,85,255);\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: rgb(148, 146, 149);\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/login/images/safe.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.login_btn.setIcon(icon2)
        self.login_btn.setObjectName("login_btn")
        self.gridLayout.addWidget(self.login_btn, 2, 0, 1, 2)
        self.pwd_le = QtWidgets.QLineEdit(self.widget_3)
        self.pwd_le.setMinimumSize(QtCore.QSize(0, 45))
        self.pwd_le.setMaximumSize(QtCore.QSize(16777215, 45))
        self.pwd_le.setStyleSheet("QLineEdit {\n"
"    font-size: 20px;\n"
"    border: none;\n"
"    border-bottom: 1px solid gray;\n"
"    background-color: transparent;\n"
"}\n"
"QLineEdit: hover{\n"
"    border-bottom: 1px solid black;\n"
"}\n"
"QLineEdit: focus \n"
"{\n"
"     border-bottom: 1px solid rgb(18,183,245);\n"
"}")
        self.pwd_le.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwd_le.setObjectName("pwd_le")
        self.gridLayout.addWidget(self.pwd_le, 1, 0, 1, 2)
        self.horizontalLayout.addWidget(self.widget_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.login_bottom)
        self.pushButton_2.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_2.setMaximumSize(QtCore.QSize(80, 80))
        self.pushButton_2.setStyleSheet("border-image: url(G:/Actionfall/resource/images/paper.jpg);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 6)
        self.horizontalLayout.setStretch(2, 2)
        self.verticalLayout.addWidget(self.login_bottom)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 3)

        self.retranslateUi(Form)
        self.pushButton.clicked['bool'].connect(Form.show_register_pane)
        self.pushButton_2.clicked.connect(Form.open_link)
        self.pwd_le.textChanged['QString'].connect(Form.enable_login_btn)
        self.account_cb.editTextChanged['QString'].connect(Form.enable_login_btn)
        self.login_btn.clicked.connect(Form.check_login)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "登录与注册"))
        self.pushButton.setText(_translate("Form", "注册账号"))
        self.account_cb.setItemText(0, _translate("Form", "abc"))
        self.account_cb.setItemText(1, _translate("Form", "234567"))
        self.login_btn.setText(_translate("Form", "安全登录"))
import source_rc
