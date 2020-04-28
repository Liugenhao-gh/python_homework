# -*- encoding: utf-8 -*-
'''
@File : 3_mutillprocess.py
@Time : 2020/04/26 17:28:51
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib
'''多进程练习：
计算1～100000之间所有素数的个数， 要求如下:
- 编写函数判断一个数字是否为素数，然后统计素数的个数；
-对比1: 对比使用多进程和不使用多进程两种方法的统计速度。
-对比2：对比开启4个多进程和开启10个多进程两种方法的速度。'''
import math
import time
from multiprocessing import Pool, Manager



def issushu(num):
    t = int(math.sqrt(num))
    for i in range(2, t+1):
        if num % i == 0:
            return False
    else:
        return True
# 计数
def counter(begin, end, queue):
    count = 0
    if begin <= 1:
        begin = 2
    for i in range(begin, end):
        if issushu(i):
            count +=1
    queue.put(count)
# 不用多进程
def not_mutilprocessing(q):
    c = 0
    start = time.process_time()
    counter(1, 100001, q)
    while(not q.empty()):
        c += q.get()
    print(c)
    end = time.process_time()
    print('time used {}'.format(end-start))
# 4个多进程

def mutillprocess_4(q):
    start = time.process_time()
    c = 0
    po= Pool(4)
    for i in range(0, 4):
        po.apply_async(counter,(i*25000, (i+1)*25000+1, q,))
    po.close()
    po.join()
    while(not q.empty()):
        c += q.get()
    print(c)
    end = time.process_time()
    print('time used {}'.format(end-start))
# 10 个多进程
def mutillprocess_10(q):
    start = time.process_time()
    c = 0
    po= Pool(10)
    for i in range(0, 10):
        po.apply_async(counter,(i*10000, (i+1)*10000+1, q,))
    po.close()
    po.join()
    while(not q.empty()):
        c += q.get()
    print(c)
    end = time.process_time()
    print('time used {}'.format(end-start))
if __name__ == "__main__":
    q = Manager().Queue()
    print('one process:')
    not_mutilprocessing(q)
    print('4 processes:')
    mutillprocess_4(q)
    print('10 processes')
    mutillprocess_10(q)
