# coding: utf-8
import os
import socket
import sqlite3
import select
import sys
from header import *

HOST = '127.0.0.1'
PORT = 8888
BUFFER_SIZE = 4096


# s发送给所有其他的socket
def send_to_others(s, data):
    for c in connections:
        if c != sock and c != s:
            c.sendall(data.encode('utf-8'))


# 对client发来的data进行处理，s是client的socket
def handle(s, data):
    print("handler>data:", data)
    h = data[0:3].decode('utf-8')
    print('h = ' + h)
    h = int(h)
    if h == c_send_file:
        # splt[1]是接收者 splt[2]是文件名 splt[3]是数据
        # 服务器发出去的：
        # s_send_file + sender + 文件名 + 数据
        print('handle c_send_file')
        '''
        sender = users[s]
        usernames = splt[1].split('\t')
        print('rev:')
        print(usernames)
        msg = (str(s_send_file) + '\r\n' + sender + splt[2]).encode('utf-8') + splt[3]
        for username in usernames:
            rev = connects[username]
            if rev is not None:
                rev.sendall(msg)
        '''
        for c in connections:
            if c != sock and c != s:
                c.sendall(str(s_send_file).encode('utf-8') + data[3:])
        print('send file done')
        return
    else:
        splt = data.decode('utf-8').split('\r\n')
        splt[0] = int(splt[0])
    if splt[0] == c_logout:
        print('handle c_logout')
        out_user = users[s]
        dt = str(s_logout) + '\r\n' + out_user
        send_to_others(s, dt)
        connections.remove(s)
        users[s] = None
        connects[out_user] = None
    elif splt[0] == c_login:
        # 在数据库中查找user
        cursor.execute("select * from user where username = '{0}' and password = '{1}'".format(splt[1], splt[2]))
        user = cursor.fetchone()
        if user is None:
            s.sendall(str(s_password_wrong).encode('utf-8'))
            print('password wrong')
        elif user[0] in connects.keys():
            # 用户已经登陆了
            s.sendall(str(s_login_repeat).encode('utf-8'))
            print('login repeat')
        else:
            # 登录成功
            connects[user[0]] = s
            users[s] = user[0]
            print(user[0])
            # 给这个socket发送login_success
            s.sendall((str(s_login_success) + '\r\n' + user[0]).encode('utf-8'))
            print('login success' + user[0])
            # s向其他socket发送新登录的用户名
            print('send: ' + str(s_new_login) + '\r\n' + str(user[0]))
            send_to_others(s, str(s_new_login) + '\r\n' + str(user[0]))
            print('send new login success' + user[0])
    elif splt[0] == c_register:
        cursor.execute("select * from user where username = '{0}'".format(splt[1]))
        user = cursor.fetchone()
        if user is None:
            cursor.execute("insert into user (username, password) values ('{0}', '{1}')".format(splt[1], splt[2]))
            db.commit()
            # 注册成功
            s.sendall(str(s_register_success).encode('utf-8'))
        else:
            s.sendall(str(s_register_repeat).encode('utf-8'))
    elif splt[0] == c_get_online_users:
        send_data = str(s_online_users)
        for co in users.keys():
            if users[co] != users[s]:
                send_data = send_data + '\r\n' + users[co]
        print('In get_online_users')
        s.sendall(send_data.encode('utf-8'))
    elif splt[0] == c_send_msg:
        print('handle c_send_msg')
        sender = users[s]
        usernames = splt[1].split('\t')
        print('rev:')
        print(usernames)
        msg = (str(s_send_msg) + '\r\n' + sender + '\r\n' + splt[2]).encode('utf-8')
        print('msg: ' + str(s_send_msg) + '\r\n' + sender + '\r\n' + splt[2])
        for username in usernames:
            rev = connects[username]
            if rev is not None:
                rev.sendall(msg)
        print('send msg done')



if __name__ == '__main__':
    # 连接数据库，没有会自动创建文件
    if not os.path.exists("info.db"):
        conn = sqlite3.connect("info.db")
        c = conn.cursor()
        c.execute('CREATE TABLE user(username TEXT PRIMARY KEY NOT NULL, password TEXT)')
        conn.commit()
        conn.close()

    db = sqlite3.connect('info.db')
    cursor = db.cursor()
    db.commit()

    # 初始化socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen(5)
    print("server connected: ", HOST, PORT)

    # Sockets from which we expect to read
    # 所有socket的合集
    connections = [sock]

    # Sockets to which we expect to write
    outputs = []

    users = {}  # 记录在线的客户端的套接字，可以从socket得到user
    connects = {}  # 将聊天双方的套接字绑定在一起，可以从user得到socket

    while True:
        # 开始select 监听, 对input_list 中的服务器端server 进行监听
        readable, writable, exceptional = select.select(connections, outputs, [])
        # handle inputs
        # 循环判断是否有客户端连接进来, 当有客户端连接进来时select将触发
        for s in readable:
            # 有新用户连接
            if s == sock:
                conn, client_address = s.accept()
                connections.append(conn)
                users[conn] = None
            # 老用户发来信息，需要处理
            else:
                try:
                    data = s.recv(BUFFER_SIZE)
                    assert len(data) > 0, 'server receive empty message'
                    handle(s, data)
                except  Exception:
                    sock.close()
                    sys.exit()

        # 处理异常的情况
        for s in exceptional:
            print('exception condition on', s.getpeername())
            # Stop listening for input on the connection
            connections.remove(s)
            if s in outputs:
                outputs.remove(s)
            sock.close()
            sys.exit()
