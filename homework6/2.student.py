# -*- encoding: utf-8 -*-
'''
@File : 2.student.py
@Time : 2020/04/14 19:36:33
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib
'''二 定义一个学生Student类。有下面的类属性：
1 姓名 name
2 年龄 age
3 成绩 score（语文，数学，英语) [每课成绩的类型为整数]
类方法：
1 获取学生的姓名：get_name() 返回类型:str
2 获取学生的年龄：get_age() 返回类型:int
3 返回3门科目中最高的分数。get_course() 返回类型:int
写好类以后，可以定义2个同学测试下:'''
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
stu1 = Student("amy",12)
stu2 = Student('Tony',12)
print(stu1.get_name(),stu1.get_age(), stu2.get_name(), stu2.get_age())