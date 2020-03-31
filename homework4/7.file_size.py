# -*- encoding: utf-8 -*-
'''
@File : 7.file_size.py
@Time : 2020/03/31 18:56:53
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib
import os 
path = r"test\homework4"
dir_list = os.listdir(path)
size = 0
for dirname in dir_list:
    dir_path = path +'\\'+dirname
    size += os.path.getsize(dir_path)
print(size)