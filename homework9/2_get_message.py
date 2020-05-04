# -*- encoding: utf-8 -*-
'''
@File : 2_get_message.py
@Time : 2020/05/03 19:38:13
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib

'''编写一个接收数据的网络程序，由“网络调试工具”发送数据，你的程序接收数据并打印输出；'''
import socket

def get_and_print():
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    
    local_addr=('',9999)

    udp_socket.bind(local_addr)
    flag = True
    while flag:

        # 接收数据
            recv_data = udp_socket.recvfrom(1024)  # 1024表示本次接收的最大字节数
        # 打印显示接收到的数据
            print(recv_data)

            print(recv_data[0].decode('gbk'))
            print(recv_data[1])
    # 关闭套接字
    udp_socket.close()

if __name__ == "__main__":
    get_and_print()
