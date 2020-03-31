# -*- encoding: utf-8 -*-
'''
@File : 5.copy.py
@Time : 2020/03/31 18:14:18
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib

with open(r"test\homework4\account&password.txt", "r") as f:
    text = f.read()

with open(r"test\homework4\copycoal.txt","w") as f:
    f.write(text)