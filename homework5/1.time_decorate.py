# -*- encoding: utf-8 -*-
'''
@File : 5.1.py
@Time : 2020/04/10 11:43:19
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib


# here put the import lib
import time
def times(func):
    def inner():
        start = time.perf_counter()
        func()
        end = time.perf_counter()
        print(end-start)
    return inner
@times
def func():
    j=0
    for i in range(10):
        j+=i
        time.sleep(1)
    print(j)

func()