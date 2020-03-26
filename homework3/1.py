# -*- encoding: utf-8 -*-
'''
@File : 1.py
@Time : 2020/03/20 17:17:45
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib

'''
1 写一个程序，读取键盘输入的任意行文字信息，当输入空行时结束输入，
将读入的字符串存于列表;然后将列表里面的内容写入到文件input.txt中；
'''
with open(r"test\homework3\input.txt",'w',encoding='utf-8') as f:
    ss = input()
    contents = []
    while ss != '':
        contents.append(ss+"\n")
        ss = input()
    f.writelines(contents[:])
