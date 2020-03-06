# -*- encoding: utf-8 -*-
'''
@File : 5_random2list_tuple.py
@Time : 2020/03/06 17:24:45
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib
from random import randint
data1=[randint(-10,10) for _ in range(10)]
data2 = tuple([randint(-10,10) for _ in range(10)])

print(data1)
print(data2)