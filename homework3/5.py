# -*- encoding: utf-8 -*-
'''
@File : 5.py
@Time : 2020/03/24 17:29:23
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib

'''
文件编程小项目
'''
# import os
# print(os.getcwd())
all = []
with open(r"test\homework3\blowing in the wind.txt",'r') as f:
    all = f.readlines()

all.insert(0,"Blowin' in the wind\n")
all.insert(1,"Bob Dylan\n")
all.append("\n1962 by Warner Bros.Inc.")  

with open(r"test\homework3\blowing in the wind.txt",'w') as f:
    for line in all:
        f.write(line)