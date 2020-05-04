# -*- encoding: utf-8 -*-
'''
@File : upd_server.py
@Time : 2020/05/03 20:10:37
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib
'''server'''
'''编写一个UDP的聊天程序，客户端和服务器端能互相聊天应答；客户端先发送；'''
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口:
send_addr = ('192.168.1.103', 9999)
s.bind(('192.168.1.103', 8888))
print('Server send UDP to {}...'.format(send_addr))
print('Server bind UDP on {}...'.format(8888))

while True:
    # 接收数据: 
    data, addr = s.recvfrom(1024)
    print('Received from {}:{}.'.format(addr, data.decode('utf-8')))
    message = input('you sends: ')
    s.sendto(message.encode('utf-8'),send_addr)
   