# -*- encoding: utf-8 -*-
'''
@File : 7_score.py
@Time : 2020/03/14 17:00:04
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib
'''
随机生成20个学生的成绩; 判断这20个学生成绩的等级; 用函数来实现;  
    A---成绩>=90;  
    B-->成绩在 [80,90)
    C-->成绩在 [70,80)
    D-->成绩<70
'''
from random import randint

def score_class(score):
    for k, v in score.items():
        if v >= 90:
            print("同学{}的成绩是A级".format(k))
        elif v>= 80 and v<= 90:
            print("同学{}的成绩是B级".format(k))
        elif v>=70 and v<=80:
            print("同学{}的成绩是C级".format(k))
        elif v<70 :
            print("同学{}的成绩是D级".format(k))

if __name__ == "__main__":
    score1 = {
        "one":1,
        "two":2,
        "three":3,
        "four":4,
        "five":5,
        "six":6,
        "seven":7,
        "eight":8,
        "nine":9,
        "ten":10
    }
    score2 = [randint(0,100) for _ in range(0,10)]
    i = 0
    score = {}
    for k in score1.keys():
        score[k] = score2[i]
        i+=1
    score_class(score)
