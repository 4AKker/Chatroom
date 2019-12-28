# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import socket
from header import *
import os

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(782, 602)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 110, 151, 461))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_users = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_users.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_users.setObjectName("gridLayout_users")
        self.userbox_4 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.userbox_4.setObjectName("userbox_4")
        self.gridLayout_users.addWidget(self.userbox_4, 3, 0, 1, 1)
        self.userbox_1 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.userbox_1.setObjectName("userbox_1")
        self.gridLayout_users.addWidget(self.userbox_1, 0, 0, 1, 1)
        self.userbox_7 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.userbox_7.setObjectName("userbox_7")
        self.gridLayout_users.addWidget(self.userbox_7, 6, 0, 1, 1)
        self.userbox_2 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.userbox_2.setObjectName("userbox_2")
        self.gridLayout_users.addWidget(self.userbox_2, 1, 0, 1, 1)
        self.userbox_5 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.userbox_5.setObjectName("userbox_5")
        self.gridLayout_users.addWidget(self.userbox_5, 4, 0, 1, 1)
        self.userbox_8 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.userbox_8.setObjectName("userbox_8")
        self.gridLayout_users.addWidget(self.userbox_8, 7, 0, 1, 1)
        self.userbox_6 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.userbox_6.setObjectName("userbox_6")
        self.gridLayout_users.addWidget(self.userbox_6, 5, 0, 1, 1)
        self.userbox_3 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.userbox_3.setObjectName("userbox_3")
        self.gridLayout_users.addWidget(self.userbox_3, 2, 0, 1, 1)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(192, 31, 551, 541))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_right = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_right.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_right.setObjectName("gridLayout_right")
        self.textBrowser = QtWidgets.QTextBrowser(self.layoutWidget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_right.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.btn_logout = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_logout.setObjectName("btn_logout")
        self.gridLayout_right.addWidget(self.btn_logout, 3, 0, 1, 1)
        self.gridLayout_rightdown = QtWidgets.QGridLayout()
        self.gridLayout_rightdown.setObjectName("gridLayout_rightdown")
        self.textEdit = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_rightdown.addWidget(self.textEdit, 0, 0, 2, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 78, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_rightdown.addItem(spacerItem, 0, 1, 2, 1)
        self.send_file = QtWidgets.QPushButton(self.layoutWidget)
        self.send_file.setObjectName("send_file")
        self.gridLayout_rightdown.addWidget(self.send_file, 0, 2, 1, 1)
        self.send = QtWidgets.QPushButton(self.layoutWidget)
        self.send.setObjectName("send")
        self.gridLayout_rightdown.addWidget(self.send, 1, 2, 1, 1)
        self.gridLayout_right.addLayout(self.gridLayout_rightdown, 2, 0, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(40, 30, 153, 81))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_leftup = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_leftup.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_leftup.setObjectName("verticalLayout_leftup")
        self.horizontalLayout_leftup = QtWidgets.QHBoxLayout()
        self.horizontalLayout_leftup.setObjectName("horizontalLayout_leftup")
        self.btn_choose_all = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_choose_all.setObjectName("btn_choose_all")
        self.horizontalLayout_leftup.addWidget(self.btn_choose_all)
        self.btn_choose_none = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_choose_none.setObjectName("btn_choose_none")
        self.horizontalLayout_leftup.addWidget(self.btn_choose_none)
        self.verticalLayout_leftup.addLayout(self.horizontalLayout_leftup)
        self.welcome_label = QtWidgets.QLabel(self.layoutWidget1)
        self.welcome_label.setObjectName("welcome_label")
        self.verticalLayout_leftup.addWidget(self.welcome_label)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 41, 601))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 570, 741, 31))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(40, 0, 701, 31))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(740, 0, 41, 571))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.btn_choose_all.setStyleSheet("QPushButton:pressed{color:black;\
                                background-color:rgb(210,255,240);}")
        self.btn_choose_none.setStyleSheet("QPushButton:pressed{color:black;\
                                background-color:rgb(210,255,240);}")
        self.send.setStyleSheet("QPushButton:pressed{color:black;\
                                background-color:rgb(210,255,240);}")
        self.send_file.setStyleSheet("QPushButton:pressed{color:black;\
                                background-color:rgb(210,255,240);}")
        self.btn_logout.setStyleSheet("QPushButton:pressed{color:black;\
                                background-color:rgb(210,255,240);}")

        self.welcome_label.setStyleSheet("font-size: 20px; font-family: Microsoft YaHei;\
                                border-width: 1px; border-style: solid;\
                                border-color: rgb(100, 100, 160);")
        self.textBrowser.setStyleSheet("font-size: 18px")

        Form.setStyleSheet("border-image: url('./image/chat_bg')")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Chatroom"))
        self.userbox_4.setText(_translate("Form", "NULL"))
        self.userbox_1.setText(_translate("Form", "NULL"))
        self.userbox_7.setText(_translate("Form", "NULL"))
        self.userbox_2.setText(_translate("Form", "NULL"))
        self.userbox_5.setText(_translate("Form", "NULL"))
        self.userbox_8.setText(_translate("Form", "NULL"))
        self.userbox_6.setText(_translate("Form", "NULL"))
        self.userbox_3.setText(_translate("Form", "NULL"))
        self.btn_logout.setText(_translate("Form", "退出"))
        self.send_file.setText(_translate("Form", "发送文件"))
        self.send.setText(_translate("Form", "发送"))
        self.btn_choose_all.setText(_translate("Form", "全选"))
        self.btn_choose_none.setText(_translate("Form", "全不选"))
        self.welcome_label.setText(_translate("Form", "欢迎你，"))


class ChatWindow(QtWidgets.QWidget, Ui_Form):
    online_users = []

    ADD_BOX = QtCore.pyqtSignal(str)
    DEL_BOX = QtCore.pyqtSignal(str)
    WELCOME = QtCore.pyqtSignal(str)
    REVMSG = QtCore.pyqtSignal(str)
    APPEND = QtCore.pyqtSignal(str)
    REV_FILE = QtCore.pyqtSignal(str, bytes)
    SHOW = QtCore.pyqtSignal()

    def __init__(self, sock, parent=None):
        super(ChatWindow, self).__init__(parent)
        self.setupUi(self)
        self.sock = sock

        self.user_in_box = ['', '', '', '', '', '', '', '']
        self.check_boxes = [self.userbox_1, self.userbox_2, self.userbox_3, self.userbox_4,
                            self.userbox_5, self.userbox_6, self.userbox_7, self.userbox_8]

        self.ADD_BOX.connect(self.add_box)
        self.DEL_BOX.connect(self.del_box)
        self.WELCOME.connect(self.welcome)
        self.REVMSG.connect(self.revmsg)
        self.SHOW.connect(self.show)
        self.APPEND.connect(self.append)
        self.REV_FILE.connect(self.rev_file)

        self.btn_choose_all.pressed.connect(self.choose_all)
        self.btn_choose_none.pressed.connect(self.choose_none)
        self.btn_logout.pressed.connect(self.logout)
        self.send.pressed.connect(self.sendmsg)
        self.send.pressed.connect(self.textEdit.clear)
        self.send_file.pressed.connect(self.sendfile)

    def sendfile(self):
        file_path = QtWidgets.QFileDialog.getOpenFileName(self, '选择文件', '')
        file_name = os.path.basename(file_path[0])

        print(file_path)

        send_data = str(c_send_file)
        '''
        flag = 0
        for i in range(0, 8):
            if self.user_in_box[i] != '' and self.check_boxes[i].isChecked():
                if flag == 0:
                    send_data = send_data + '\r\n' + self.user_in_box[i]
                    flag = 1
                else:
                    send_data = send_data + '\t' + self.user_in_box[i]
        if flag == 0:
            send_data = send_data + '\r\n'
        '''
        f = open(file_path[0], "rb")
        data = f.read()
        # send_data = (send_data + '\r\n' + file_name + '\r\n').encode('utf-8') + data
        send_data = send_data.encode('utf-8') + data
        self.sock.sendall(send_data)
        self.APPEND.emit('I send file:\n' + file_path[0])

    def rev_file(self, filename, file):
        reply = QtWidgets.QMessageBox.question(self, "文件", "\n是否要接收文件？", QtWidgets.QMessageBox.No |
                                       QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            f = open(filename, "wb+")
            f.write(file)
            QtWidgets.QMessageBox.information(self, "成功", "\n存储为{}".format(filename), QtWidgets.QMessageBox.Ok)

    def logout(self):
        self.sock.sendall(str(c_logout).encode('utf-8'))
        self.close()

    def append(self, msg):
        self.textBrowser.append(msg)

    def choose_all(self):
        self.userbox_1.setChecked(True)
        self.userbox_2.setChecked(True)
        self.userbox_3.setChecked(True)
        self.userbox_4.setChecked(True)
        self.userbox_5.setChecked(True)
        self.userbox_6.setChecked(True)
        self.userbox_7.setChecked(True)
        self.userbox_8.setChecked(True)

    def choose_none(self):
        self.userbox_1.setChecked(False)
        self.userbox_2.setChecked(False)
        self.userbox_3.setChecked(False)
        self.userbox_4.setChecked(False)
        self.userbox_5.setChecked(False)
        self.userbox_6.setChecked(False)
        self.userbox_7.setChecked(False)
        self.userbox_8.setChecked(False)

    def sendmsg(self):
        send_data = str(c_send_msg)
        msg = self.textEdit.toPlainText()
        flag = 0
        for i in range(0, 8):
            if self.user_in_box[i] != '' and self.check_boxes[i].isChecked():
                if flag == 0:
                    send_data = send_data + '\r\n' + self.user_in_box[i]
                    flag = 1
                else:
                    send_data = send_data + '\t' + self.user_in_box[i]
        if flag == 0:
            send_data = send_data + '\r\n'
        send_data = send_data + '\r\n' + msg
        self.sock.sendall(send_data.encode('utf-8'))
        self.textBrowser.append('I say:')
        self.textBrowser.append(msg)
        self.textBrowser.moveCursor(self.textBrowser.textCursor().End)  # 文本框显示到底部

    def revmsg(self, msg):
        splt = msg.split('\r\n')
        sender = splt[0]
        mg = splt[1]
        self.textBrowser.append(sender + ' says:')
        self.textBrowser.append(mg)
        self.textBrowser.moveCursor(self.textBrowser.textCursor().End)  # 文本框显示到底部

    def add_box(self, username):
        _translate = QtCore.QCoreApplication.translate
        if self.user_in_box[0] == '':
            self.userbox_1.setText(_translate("Form", username))
            self.userbox_1.setChecked(True)
            self.user_in_box[0] = username
        elif self.user_in_box[1] == '':
            self.userbox_2.setText(_translate("Form", username))
            self.userbox_2.setChecked(True)
            self.user_in_box[1] = username
        elif self.user_in_box[2] == '':
            self.userbox_3.setText(_translate("Form", username))
            self.userbox_3.setChecked(True)
            self.user_in_box[2] = username
        elif self.user_in_box[3] == '':
            self.userbox_4.setText(_translate("Form", username))
            self.userbox_4.setChecked(True)
            self.user_in_box[3] = username
        elif self.user_in_box[4] == '':
            self.userbox_5.setText(_translate("Form", username))
            self.userbox_5.setChecked(True)
            self.user_in_box[4] = username
        elif self.user_in_box[5] == '':
            self.userbox_6.setText(_translate("Form", username))
            self.userbox_6.setChecked(True)
            self.user_in_box[5] = username
        elif self.user_in_box[6] == '':
            self.userbox_7.setText(_translate("Form", username))
            self.userbox_7.setChecked(True)
            self.user_in_box[6] = username
        elif self.user_in_box[7] == '':
            self.userbox_8.setText(_translate("Form", username))
            self.userbox_8.setChecked(True)
            self.user_in_box[7] = username

    def del_box(self, username):
        _translate = QtCore.QCoreApplication.translate
        if self.user_in_box[0] == username:
            self.userbox_1.setText(_translate("Form", 'NULL'))
            self.userbox_1.setChecked(False)
            self.user_in_box[0] = ''
        elif self.user_in_box[1] == username:
            self.userbox_2.setText(_translate("Form", 'NULL'))
            self.userbox_2.setChecked(False)
            self.user_in_box[1] = ''
        elif self.user_in_box[2] == username:
            self.userbox_3.setText(_translate("Form", 'NULL'))
            self.userbox_3.setChecked(False)
            self.user_in_box[2] = ''
        elif self.user_in_box[3] == username:
            self.userbox_4.setText(_translate("Form", 'NULL'))
            self.userbox_4.setChecked(False)
            self.user_in_box[3] = ''
        elif self.user_in_box[4] == username:
            self.userbox_5.setText(_translate("Form", 'NULL'))
            self.userbox_5.setChecked(False)
            self.user_in_box[4] = ''
        elif self.user_in_box[5] == username:
            self.userbox_6.setText(_translate("Form", 'NULL'))
            self.userbox_6.setChecked(False)
            self.user_in_box[5] = ''
        elif self.user_in_box[6] == username:
            self.userbox_7.setText(_translate("Form", 'NULL'))
            self.userbox_7.setChecked(False)
            self.user_in_box[6] = ''
        elif self.user_in_box[7] == username:
            self.userbox_8.setText(_translate("Form", 'NULL'))
            self.userbox_8.setChecked(False)
            self.user_in_box[7] = ''

    def welcome(self, username):
        _translate = QtCore.QCoreApplication.translate
        self.welcome_label.setText(_translate("Form", str("欢迎你，" + username)))


if __name__ == "__main__":
    import sys
    sock = socket.socket()
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = ChatWindow(sock)
    ui.setupUi(Form)
    Form.show()

    '''
    ui.ADD_BOX.emit('qwe')
    s = input()
    if s == 'a':
        ui.ADD_BOX.emit('asd')
    sleep(1)
    ui.DEL_BOX.emit('qwe')
    '''

    sys.exit(app.exec_())

