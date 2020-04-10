# -*- encoding: utf-8 -*-
'''
@File : 2.log_decorate.py
@Time : 2020/04/10 11:53:18
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib


# here put the import lib
import datetime,os
def record(func):
    def inner():
        t=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(func,t)
        func()
        try:
            with open(r'test\homework5\log.txt','w',encoding='utf-8') as f:
                s='{}{} \n'.format(func,t)
                f.write(s)
        except IOError:
            print('error')
    return inner

@record
def a():
    j=0
    for i in range(10):
        j+=i
    print('try one',j)
a()


