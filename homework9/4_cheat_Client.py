# -*- encoding: utf-8 -*-
'''
@File : cheat_Client.py
@Time : 2020/05/04 10:43:43
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib

import socket
import threading
import os


class Client:
    def __init__(self):
        # 创建套接字
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        # 连接

        self.addr = ('192.168.1.103', 9999)
        try:
            self.s.connect(self.addr)
            print('服务器已连接')
        except ConnectionRefusedError:
            print('服务器连接失败')
            os._exit(0)
        
    # 接收信息
    def recv(self):
        while True:
            try:
                response = self.s.recv(1024)
                print(':'+response.decode('utf-8'))
            except ConnectionResetError:
                print('服务器已关闭，聊天结束')
                self.s.close()
                break
        os._exit(0)

    def send(self):
        print('按回车发送消息')
        print('输入\'esc\'退出程序')
        while True:
            message = input()
            if message =='esc':
                print('聊天结束')
                self.s.close()
                break
            else:
                self.s.send(message.encode('utf-8'))

        os._exit(0)
    
    def start(self):
        threads = [threading.Thread(target=self.recv), threading.Thread(target=self.send)]
        for t in threads:
            t.start()

if __name__ == "__main__":
    C = Client()
    C.start()
