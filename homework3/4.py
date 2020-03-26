# -*- encoding: utf-8 -*-
'''
@File : 4.py
@Time : 2020/03/24 16:42:54
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib
'''
 在当前目录新建目录img, 里面包含10个文件, 10个文件名各不相同(X4G5.png)
 将当前img目录所有以.png结尾的后缀名改为.jpg.
'''
import os
dirpath = r"test\homework3\img"
filename = os.listdir(dirpath)
for n in filename:
    allname = os.path.splitext(n)
    if allname[1] == ".png":
        newname = allname[0]+".jpg"
        os.rename(dirpath+"\\"+n, dirpath+"\\"+newname)

