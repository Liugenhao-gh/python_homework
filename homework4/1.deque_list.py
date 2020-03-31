# -*- encoding: utf-8 -*-
'''
@File : 1.deque_list.py
@Time : 2020/03/31 15:41:56
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib
from collections import deque
import time
list_1 = [1,2,3,4,5,6,7,8,9,0]
start = time.perf_counter()
list_1.insert(0, 98)
list_1.append(99)
end = time.perf_counter()
print(start-end)

q = deque(list_1)
start = time.perf_counter()
q.append(100)
q.appendleft(101)
end = time.perf_counter()
print(start-end)