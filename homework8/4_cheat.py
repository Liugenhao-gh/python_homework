# -*- encoding: utf-8 -*-
'''
@File : 4_cheat.py
@Time : 2020/04/27 18:05:05
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib

'''多进程通讯：
  编写一个简单的聊天程序；其中一个进程发送文字聊天消息（从键盘输入文字消息）； 
  另外一个进程接收并打印消息；'''
from multiprocessing import Process, Queue

def sender(queue, r):
    # expression = input('>')
    try:
        while True:
            queue.put(input('主进程：'))
    except EOFError:
        print('stop')
        r.terminate()
    
def receiver(queue):
    while True:
        print('receive: {}'.format(queue.get()))

if __name__ == '__main__':
    q = Queue()
    
    r = Process(target=receiver, args=(q,))
    r.start()
    print('\'ctrl + z\' to stop')
    sender(q,r)