# -*- encoding: utf-8 -*-
'''
@File : 4.student2.py
@Time : 2020/04/14 19:56:40
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib
'''封装一个学生类，有姓名，有年龄，有性别，有英语成绩，数学成绩，语文成绩，
封装方法，求单个学生的总分，平均分，以及打印学生的信息。'''

class Student2:
    def __init__(self, name, age, sex, English, Math, Chinese):
        self.name = name
        self.age = age
        self.sex = sex
        self.English = English
        self.Math = Math
        self.Chinese = Chinese
    def get_sum_score(self):
        return self.English + self.Math + self.Chinese
    
    def get_arvage_score(self):
        return self.get_sum_score()/3
    def print_message(self):
        print("""name:{}, age:{}, sex:{}, 
        score of English:{}, score of Math:{}, score of Chinese:{}""".format(self.name,self.age,self.sex,self.English,self.Math,self.Chinese))

stu = Student2('Tony',12,'boy',123,123,222)
print(stu.get_sum_score(), stu.get_arvage_score())
stu.print_message()