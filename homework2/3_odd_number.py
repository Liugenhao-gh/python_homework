# -*- encoding: utf-8 -*-
'''
@File : 3_odd_number.py
@Time : 2020/03/12 12:37:53
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib

'''
编写一个函数, 传入一个数字列表, 输出列表中的奇数;
   数字列表请用随机数函数生成;
'''
def odd_number(a):
    """a is a list"""
    odd = []
    for i in a:
        if i%2 == 1:
            odd.append(i)
    return odd

if __name__ == "__main__":
    from random import randint
    data=[randint(-10,10) for _ in range(10)]
    print(odd_number(data))
