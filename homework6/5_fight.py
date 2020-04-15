# -*- encoding: utf-8 -*-
'''
@File : 5_fight.py
@Time : 2020/04/14 20:22:04
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib

from Dog import Dog
from People import People
from random import randint

dog = [Dog(), Dog(),Dog()]
people = [People(), People()]
def choose_attact(a,b):
    # 判断游戏是否还可以进行下去
    flag1 = True 
    flag2 = True
    for f in a:
        if f.get_blood() > 0 and f.get_attack() > 0:
            flag1 = False
    for s in b:
        if s.get_blood() > 0 and f.get_attack() > 0:
            flag2 = False
    
    if flag1:
        print(a[0].get_sort(),"defeat") 
        return False
    elif flag2:
        print(b[0].get_sort(),"defeat")
        return False
    else:
        # 可以继续进行，随机选择攻击种族和被攻击种族
        while True:
            num = randint(0, len(a)-1)
            f = a[num]
            if f.get_blood() > 0 and f.get_attack() > 0:
                attacker = f
                break
        while True:
            num = randint(0, len(b)-1)
            s = b[num]
            if s.get_blood() > 0 :
                be_attacker = s
                break
        
        print("攻击者种族{}，血量{}，攻击力{}".format(attacker.get_sort(),attacker.get_blood(),attacker.get_attack()))
        print("被攻击种族{}，血量{}，攻击力{}".format(be_attacker.get_sort(),be_attacker.get_blood(),be_attacker.get_attack()))
        be_attacker.be_attack(attacker.get_attack())
        return True
start = randint(0,1)
flag = True
p = 30
while flag:
    # 随机选择种族先攻击
    if start == 0:
        a = dog
        b = people
    elif start == 1:
        a = people
        b = dog
    start = -1
    flag = choose_attact(a,b)
    c = b
    b = a
    a = c
