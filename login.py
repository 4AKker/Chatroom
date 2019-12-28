import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from header import *

sock = None

def login_get_sock(s):
    global sock
    sock = s

class LoginWindow(QMainWindow):
    """
    聊天室的登录窗口：
    """
    # 为了能在外部调用
    CLOSE = pyqtSignal()
    LOGIN_REPEAT = pyqtSignal()
    PASSWORD_WRONG = pyqtSignal()
    REGISTER_SUCCESS = pyqtSignal()
    REGISTER_REPEAT = pyqtSignal()


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sock = sock
        # 为了能在外部调用
        self.CLOSE.connect(self.close)
        self.LOGIN_REPEAT.connect(self.login_repeat)
        self.PASSWORD_WRONG.connect(self.password_wrong)
        self.REGISTER_REPEAT.connect(self.register_repeat)
        self.REGISTER_SUCCESS.connect(self.register_success)

        # usernameLabel=QLabel("用户名：")
        # passwdLabel=QLabel("用户名：")
        # self.label=QTex
        self.label = QLabel("<h4 style='text-align:center'>LOGIN</h4>")
        # self.label=BubbleText()
        self.label.setDisabled(True)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.username = QLineEdit()
        self.username.setPlaceholderText("USERNAME")
        self.password = QLineEdit()
        self.password.setPlaceholderText("PASSWORD")
        self.password.setEchoMode(2)
        layout = QGridLayout()
        self.btnSend = QPushButton("LOGIN")
        self.btnRegister = QPushButton("REGISTER")
        self.btnQuit = QPushButton("QUIT")
        self.btnSend.pressed.connect(self.login)
        self.btnRegister.pressed.connect(self.register)
        self.btnQuit.pressed.connect(self.close)

        layout.addWidget(self.label, 0, 0, 1, 3)
        layout.addWidget(self.username, 1, 0, 2, 3)

        layout.addWidget(self.password, 3, 0, 2, 3)
        layout.addWidget(self.btnSend, 5, 0)
        layout.addWidget(self.btnRegister, 5, 1)
        layout.addWidget(self.btnQuit, 5, 2)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.btnSend.setStyleSheet("QPushButton:pressed{color:black;\
        background-color:rgb(210,255,240);}")
        self.btnQuit.setStyleSheet("QPushButton:pressed{color:black;\
        background-color:rgb(210,255,240);}")
        self.username.setStyleSheet("QLineEdit:focus{border:1px solid #aaaaf0}")
        self.password.setStyleSheet("QLineEdit:focus{border:1px solid #aaaaf0}")
        self.setStyleSheet("color:rgb(210,225,240);background-color:black")
        # self.resize(450,250)
        self.setFixedSize(320, 150)
        self.center()
        self.setWindowOpacity(0.95)

    def mousePressEvent(self, event):
        print(event.globalPos())
        self.windowPos = self.pos()
        self.mousePos = event.globalPos()
        self.dPos = self.mousePos - self.windowPos

    def mouseMoveEvent(self, event):
        print(event.globalPos())
        self.move(event.globalPos() - self.dPos)

    def center(self):
        """
        center the window
        """
        qr_ = self.frameGeometry()
        cp_ = QDesktopWidget().availableGeometry().center()
        qr_.moveCenter(cp_)
        self.move(qr_.topLeft())

    def password_wrong(self):
        QMessageBox.warning(self, "Warning", "\nWRONG USERNAME OR PASSWORD", QMessageBox.Cancel)

    def login_repeat(self):
        QMessageBox.warning(self, "Warning", "\nLOGIN REPEAT", QMessageBox.Cancel)

    def register_success(self):
        QMessageBox.information(self, "Info", "\nREGISTER SUCCESS", QMessageBox.Yes)

    def register_repeat(self):
        QMessageBox.warning(self, "Warning", "\nREGISTER REPEAT", QMessageBox.Cancel)

    def login(self):
        username = self.username.text()
        password = self.password.text()
        self.sock.sendall(('\r\n'.join([str(c_login), username, password]).encode('utf-8')))

    def register(self):
        username = self.username.text()
        password = self.password.text()
        QMessageBox.question(self, "CONFIRM", "\nAre you sure to register?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        self.sock.sendall(('\r\n'.join([str(c_register), username, password]).encode('utf-8')))

    def keyPressEvent(self, QKeyEvent):
        """
        登录对话框的按键处理函数：按下回车键或者小键盘的enter键触发点击login按钮。
        """
        if QKeyEvent.key() == Qt.Key_Return or QKeyEvent.key() == Qt.Key_Enter:
            self.btnSend.animateClick()
        if QKeyEvent.key() == Qt.Key_Escape:
            self.btnQuit.animateClick()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    loginWindow = LoginWindow()

    # loginWindow.btnSend.clicked.connect(chatWindow.handle_click)
    loginWindow.btnSend.clicked.connect(loginWindow.close)

    loginWindow.show()
    app.exec_()
