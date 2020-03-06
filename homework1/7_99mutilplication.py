# -*- encoding: utf-8 -*-
'''
@File : 7_99mutilplication.py
@Time : 2020/03/06 17:49:37
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib

for i in range(1, 10):
    for j in range(1, i+1):
        print("{}*{}={}".format(j, i, i*j), end = "\t")
    print()