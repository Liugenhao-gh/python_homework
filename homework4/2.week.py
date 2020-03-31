# -*- encoding: utf-8 -*-
'''
@File : 2.week.py
@Time : 2020/03/31 16:09:47
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib

from datetime import date, datetime

def getweek(oneday):
    """
        输入一个日期，返回这日期是这一年的第几周，和周几。
    """
    theday = datetime.strptime(oneday,"%Y-%m-%d")
    return date.strftime(theday, "%W %w").split()

if __name__ =="__main__":
    today = input("请按格式“年-月-日”输入日期>>")
    start = getweek("2020-2-17")
    theday = getweek(today)
    print("校历第{}周，周{}".format(int(theday[0])-int(start[0])+1, theday[1]))