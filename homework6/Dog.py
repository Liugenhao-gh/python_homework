# -*- encoding: utf-8 -*-
'''
@File : 5.Dog.py
@Time : 2020/04/14 20:07:43
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib
class Dog:
    def __init__(self):
        self.blood = 80
        self.attack = 15
        self.sort = 'dog'

    def be_attack(self, attack):
        self.blood -= attack
        self.attack -= 3
    def get_attack(self):
        return self.attack
    def get_blood(self):
        return self.blood
    def get_sort(self):
        return self.sort
