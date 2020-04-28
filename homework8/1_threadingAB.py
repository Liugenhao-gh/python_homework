# -*- encoding: utf-8 -*-
'''
@File : 1_threadingAB.py
@Time : 2020/04/26 14:22:27
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib

''' 有100个同学的分数：数据请用随机函数生成；
     A  利用多线程程序（比如，5个线程，每个线程负责输出20条记录），快速输出这100个同学的信息；
     B 利用线程池来实现；'''

from random import randint
import threading 
from concurrent.futures import ThreadPoolExecutor
stu_score = [randint(0,100) for i in  range(0,100)]
###  A
print('-----------------------A')
def printer(score,i):
    for l in score:
        print('第{}个线程：{}'.format(i,l))

def A(stu_score):
    for i in range(0,5):
        t = threading.Thread(target=printer,args=(stu_score[i*20:i*20+20],i,))
        t.start()
A(stu_score)
#####  B
print('-----------------------B')
def B(stu_score):
    executor = ThreadPoolExecutor(max_workers= 5)
    for i in range(0,5):
        executor.submit(printer,(stu_score[i*20:i*20+20],i,))

B(stu_score)