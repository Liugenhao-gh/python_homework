# -*- encoding: utf-8 -*-
'''
@File : 9_youGuess.py
@Time : 2020/03/06 18:36:59
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib
from random import randint
a = randint(0, 100)
n = int(input("请输入猜测次数："))
counter = 0
while (counter < n):
    b = int(input("请输入猜测数字："))
    if b == a:
        print("恭喜你{}次就猜对了。游戏结束。".format(counter+1))
    else:
        counter += 1
        print("很遗憾猜错了，还有{}次机会。".format(n-counter))
print("次数用尽，游戏结束，所猜的数字是",a)