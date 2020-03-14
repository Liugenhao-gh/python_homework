# -*- encoding: utf-8 -*-
'''
@File : 9_sort.py
@Time : 2020/03/14 17:42:42
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib
'''
定义一个函数，函数接收一个数组，
并把数组里面的数据从小到大排序(冒泡排序,  也可以直接使用相关的函数);
'''
def mysort(list1):
    return sorted(list1)

if __name__ == "__main__":
    list1 = [23,4,5,6,32]
    print(mysort(list1))
