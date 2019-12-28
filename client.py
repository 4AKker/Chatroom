# coding: utf-8
import sys
import socket
import select
import threading
from login import *
from chat import *
import random


HOST = '127.0.0.1'
PORT = 8888
BUFFER_SIZE = 4096


def receive():
    while True:
        # 开始select 监听, 对input_list 中的服务器端server 进行监听
        readable, writable, exceptional = select.select([sock], [], [])
        # handle inputs
        # 循环判断是否有客户端连接进来, 当有客户端连接进来时select将触发
        # s是client的socket，sendall发送c_开头的请求
        for s in readable:
            data = s.recv(BUFFER_SIZE)
            print('handle: ', data)
            if data[0:3].decode('utf-8') == str(200):
                print('in')
                ui_chat.REV_FILE.emit(str(int((random.random()+1)*1000)), data[3:])
                continue
            splt = data.decode('utf-8').split('\r\n')
            if splt[0] == '':
                break
            print('Receive:', splt[0])
            splt[0] = int(splt[0])
            if splt[0] == s_login_success:
                # ui_chat.setClientId(ui_login.clientId)
                ui_login.CLOSE.emit()
                print('client: login success')
                username = splt[1]
                ui_chat.SHOW.emit()
                ui_chat.WELCOME.emit(username)
                s.sendall(str(c_get_online_users).encode('utf-8'))
            elif splt[0] == s_online_users:
                # 初始化user box
                for i in range(1, len(splt)):
                    ui_chat.ADD_BOX.emit(splt[i])
            elif splt[0] == s_new_login:
                print('client: new login' + splt[1])
                ui_chat.APPEND.emit(splt[1] + '进入了聊天室')
                ui_chat.ADD_BOX.emit(splt[1])
            elif splt[0] == s_login_repeat:
                ui_login.LOGIN_REPEAT.emit()
                print('client: login repeat')
            elif splt[0] == s_password_wrong:
                ui_login.PASSWORD_WRONG.emit()
                print('client: password wrong')
            elif splt[0] == s_register_success:
                ui_login.REGISTER_SUCCESS.emit()
                print('client: register success')
            elif splt[0] == s_register_repeat:
                ui_login.REGISTER_REPEAT.emit()
                print('client: register repeat')
            elif splt[0] == s_send_msg:
                sender = splt[1]
                msg = splt[2]
                data = sender + '\r\n' + msg
                ui_chat.REVMSG.emit(data)
            elif splt[0] == s_logout:
                ui_chat.APPEND.emit(splt[1] + '退出了聊天室')
                ui_chat.DEL_BOX.emit(splt[1])
            else:
                print('client rev error')


if __name__ == '__main__':
    sock = socket.socket()
    try:
        sock.connect((HOST, PORT))
        print('Connected with server')
    except Exception as e:
        print("Fail to connect (%s, %s) due to" % (HOST, PORT), e)
        exit()

    app = QApplication(sys.argv)

    login_get_sock(sock)
    ui_login = LoginWindow()

    ui_chat = ChatWindow(sock)

    listen = threading.Thread(target=receive, args=(), daemon=True)
    listen.start()

    ui_login.show()
    app.exec_()

    sock.close()
    sys.exit()
