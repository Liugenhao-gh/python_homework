# -*- encoding: utf-8 -*-
'''
@File : element_out_find.py
@Time : 2020/03/06 16:40:26
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib
import math
# 0-50的奇数
print("0-50的奇数")
for i in range(0, 51):
    if i%2 == 1:
        print(i)


# 0-50的偶数
print("0-50的偶数")
for i in range(0, 51):
    if i%2 == 0:
        print(i)


# 0-50的质数
print("0-50的质数")
for i in range(2,51):
    for n in range(2, int(math.sqrt(i))+1):
        if i%n == 0:
            break
    else:
        print(i)