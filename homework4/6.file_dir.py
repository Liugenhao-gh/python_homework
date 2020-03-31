# -*- encoding: utf-8 -*-
'''
@File : 6.file_dir.py
@Time : 2020/03/31 18:19:42
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib

import os
from datetime import datetime
path = r"C:\Users\10481\temp\project\test"
alldir_file = os.listdir(path)
print("{:<30}{:<30}{:<30}{:<30}".format("name", "changedate","type","size"))
for fd in alldir_file:
    fdpath = path+"\\"+fd
    t = os.path.getmtime(fdpath)
    date = datetime.fromtimestamp(t).replace(microsecond=0)
    if os.path.isdir(fdpath):
        print("{:<30}{:<30}{:<30}{:<30}".format(fd, date.strftime('%Y-%m-%d %H:%M:%S'), "file",os.path.getsize(fdpath)))
    else:
        temp = os.path.splitext(fd)
        print("{:<30}{:<30}{:<30}{:<30}".format(fd, date.strftime('%Y-%m-%d %H:%M:%S'), temp[1], os.path.getsize(fdpath)))
