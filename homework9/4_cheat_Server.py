# -*- encoding: utf-8 -*-
'''
@File : cheat_Server.py
@Time : 2020/05/04 11:41:31
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib
import socket
import threading
import time
import os
class Server:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.addr =  ('192.168.1.103', 9999)
        self.user = {}
    def start_server(self):
        try :
            self.s.bind(self.addr)
            self.s.listen(5)
        except Exception as e:
            print(e)
        print('服务器已开启，等待连接')
        print('输入\'esc\'关闭服务器')
        threading.Thread(target=self.close).start()
        self.accept_connect()
        

    def accept_connect(self):
        while True:
            s, addr = self.s.accept()
            self.user[addr]= s
            num = len(self.user)
            print('user:{} online. There are {} users. '.format(addr, num))
            threading.Thread(target=self.recv_and_send2all,args=(addr,s,)).start()
    def recv_and_send2all(self, addr, socket):
        while True:
            try:
                response = socket.recv(1024).decode('utf-8')
                message = '{}:{}发来消息: {}'.format(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()),addr,response) 
                for client in self.user.values():
                    client.send(message.encode('utf-8'))
            except ConnectionResetError:
                print("用户{}已经退出聊天！".format(addr))
                self.user.pop(addr)
                break
    def close(self):
        while True:
            cmd = input()
            if cmd == 'esc':
                for client in self.user.values():
                    client.close()
                self.s.close()
                os._exit(0)
            else:
                print('命令无效')

if __name__ == "__main__":
    Server = Server()
    Server.start_server()
            