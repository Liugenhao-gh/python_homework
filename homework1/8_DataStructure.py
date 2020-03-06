# -*- encoding: utf-8 -*-
'''
@File : 8_DataStructure.py
@Time : 2020/03/06 17:59:51
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib
#每个员工信息包括：工号，姓名，工龄，工资
#将这10个员工，按照工资从高到低打印输出
employee = [
    [101, "one", 10, 1000],
    [102, "two", 11, 1001],
    [103, "three", 12, 1002],
    [104, "four", 13, 1003],
    [105, "five", 14, 1004],
    [106, "six", 15, 1006],
    [107, "seven", 16, 1007],
    [108, "eight", 17, 1008],
    [109, "night", 18, 1009],
    [110, "ten", 19, 1010]
]
for i in range(1, 10):
    index = list(range(0, i))
    index.reverse()
    temp = employee[i]
    for j in index:
        if temp[3] >employee[j][3]:
            employee[j+1] = employee[j]
    employee[j] = temp
        
for i in employee:
    print(i)