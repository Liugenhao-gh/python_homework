# -*- encoding: utf-8 -*-
'''
@File : 6_Fibonacci.py
@Time : 2020/03/06 17:31:11
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib

Fibo = [0,1]
i = 2
while(Fibo[i-2] + Fibo[i-1] < 100):
    Fibo.append( Fibo[i-2] + Fibo[i-1])
    i += 1
print(Fibo)
