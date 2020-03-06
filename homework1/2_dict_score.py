# -*- encoding: utf-8 -*-
'''
@File : dict_score.py
@Time : 2020/03/06 17:03:37
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib

score = {
    100 : 100, 
    101 : 96,
    102 : 92,
    103 : 88,
    104 : 84,
    105 : 80,
    106 : 76,
    107 : 72,
    108 : 68,
    109 : 64,
    110 : 60,
    }
for k, v in score.items():
    if v > 80:
        print("学号：{} 分数：{}".format(k, v))
