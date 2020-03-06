# -*- encoding: utf-8 -*-
'''
@File : 4_leapyear.py
@Time : 2020/03/06 17:18:27
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib
year = int(input("请任意输入一个年份>>"))

if year % 100 == 0:
    print(year,"是个闰年。")
else:
    if year % 4 == 0:
        print(year, "是个闰年。")
    else:
        print(year, "不是个闰年。")
