# -*- encoding: utf-8 -*-
'''
@File : 5.4.py
@Time : 2020/04/10 11:56:33
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib

'''编写装饰器来实现，对目标函数进行装饰，分3种情况：目标函数无参数无返回值，目标函数有参数，
目标函数有返回值；
     三个目标函数分别为：
     A 打印输出20000之内的素数；
     B 计算整数2-10000之间的素数的个数；
     C 计算整数2-M之间的素数的个数；
  可以观看给的视频材料，仿照示例来做；'''
def da(func):
    def inner():
        print('无参数无返回值：',func)
        func()
    return inner

def db(func):
    def inner(*arg):
        print('有参数：',func)
        func(*arg)
    return inner

def dc(func):
    def inner():
        print('有返回值：',func)
        r=func()
        return r
    return inner

@da
def a():
    for i in range(2,20000):
        t=1
        for j in range(2,i):
            if i%j==0:
                t=0
                break
        if t==1:
            print(i)
a()  

@db
def b(x):
     for i in range(2,x):
        t=1
        for j in range(2,i):
            if i%j==0:
                t=0
                break
        if t==1:
            print(i)
x=20
b(x)

@dc
def c():
    count=0
    for i in range(2,10000):
        t=1
        for j in range(2,i):
            if i%j==0:
                t=0
                break
        if t==1:
            count+=1
    return count
print(c())