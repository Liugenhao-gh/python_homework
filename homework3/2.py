# -*- encoding: utf-8 -*-
'''
@File : 2.py
@Time : 2020/03/20 17:28:39
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib

'''
2 写一个程序，从input.txt中读取之前输入的数据，
存入列表中，再加上行号打印显示；格式如下
#第一行： xxxx
#第二行： xxxx
'''
with open(r"test\homework3\input.txt", 'r', encoding='utf-8') as f:
    contents = f.readlines()
    for i in range(len(contents)):
        print("#第{}行：{}".format(i, contents[i]))