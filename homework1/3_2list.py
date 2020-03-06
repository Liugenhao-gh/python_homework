# -*- encoding: utf-8 -*-
'''
@File : 3_2list.py
@Time : 2020/03/06 17:13:25
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib

list_1 = list(range(1, 11))
list_2 = list(range(5, 16))

for i in list_1:
    for j in list_2:
        if i == j:
            print(i)
