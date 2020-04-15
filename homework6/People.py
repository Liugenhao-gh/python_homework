# -*- encoding: utf-8 -*-
'''
@File : 5.People.py
@Time : 2020/04/14 20:17:09
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib

class People:
    def __init__(self):
        self.blood = 100
        self.attack = 10
        self.sort = 'people'

    def be_attack(self, attack):
        self.blood -= attack
        self.attack -= 2
    def get_attack(self):
        return self.attack
    def get_blood(self):
        return self.blood
    def get_sort(self):
        return self.sort
