# -*- encoding: utf-8 -*-
'''
@File : udp_client.py
@Time : 2020/05/03 19:50:02
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib
'''client'''
'''编写一个UDP的聊天程序，客户端和服务器端能互相聊天应答；客户端先发送；'''
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口:
send_addr = ('192.168.1.103', 8888)
s.bind(('192.168.1.103', 9999))
print('Client send UDP to {}...'.format(send_addr))
print('Client bind UDP on {}...'.format(9999))

while True:
    # 发送数据:
    message = input('you sends: ')
    s.sendto(message.encode('utf-8'),send_addr)
    data, addr = s.recvfrom(1024)
    print('Received from {}:{}.'.format(addr, data.decode('utf-8')))
   