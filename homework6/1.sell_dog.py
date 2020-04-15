# -*- encoding: utf-8 -*-
'''
@File : 1.sell_dog.py
@Time : 2020/04/10 12:12:22
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib

'''定义一个狗类,里面有一个 列表成员变量(列表的元素是字典), 分别记录了 3种颜色的狗的颜色, 数量,和价格;
实现狗的买卖交易方法;  打印输出经过2-3次买卖方法后,剩下的各类狗的数量;'''

class Dog:

    def __init__(self):
        self.all = [
            {'color' : 'black', 'num' : 10, 'price' : 100},
            {'color' : 'blue', 'num' : 10, 'price' : 90},
            {'color' : 'red', 'num' : 10, 'price' : 10},
        ]
    
    def print_rest(self):
        for item in self.all:
            print(item['color'], item['num'], item['price'])
        
    def buy_dog(self, color, num):
        for i in range(len(self.all)):
            if self.all[i]['color'] == color:
                self.all[i]['num'] += num
    def sell_dog(self, color, num):
        for i in range(len(self.all)):
            if self.all[i]['color'] == color:
                self.all[i]['num'] -= num

dog = Dog()
dog.sell_dog('black', 10)
dog.sell_dog('blue', 10)
dog.buy_dog('black',9)
dog.print_rest()