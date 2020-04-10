# -*- encoding: utf-8 -*-
'''
@File : 3.password_decorate.py
@Time : 2020/04/10 11:55:13
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib

def  check(func):
    def inner():
        x=input('输入账号')
        y=input('输入密码')
        if x=='123' and y=='123':
            func()
        else:
            print('账号或密码错误,不能使用该函数')
    return inner
@check
def abc():
    print(1)
abc()