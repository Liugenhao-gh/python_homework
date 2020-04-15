# -*- encoding: utf-8 -*-
'''
@File : 6_python_score.py
@Time : 2020/04/15 17:30:22
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib
'''用面向对象,实现一个学生Python成绩管理系统;
      学生的信息存储在文件中;学生信息的字段有(班级,学号,姓名, Python成绩)
      实现对学生信息及成绩的增,删,改,查方法;'''
class python_score:
    message_list = []
    def save(self):
        with open(r'test\homework6\python_sore.txt', 'w',encoding = 'utf-8') as f:
            for i in self.message_list:
                f.write(' '.join(str(j) for j in i)+'\n')
        self.message_list.clear()
    def get(self):
        with open(r'test\homework6\python_sore.txt', 'r',encoding = 'utf-8') as f:
            for line in f.readlines():
                self.message_list.append(line.split())
    def __init__(self,message):
        self.message_list = message
        self.save()
    def add(self):
        '''
        增
        '''
        class_student = input("input class:")
        ID_student = input("input ID:")
        name_student = input("input name:")
        score_student = input("input python score:")
        message_line = [class_student, ID_student, name_student, score_student]
        self.get()
        self.message_list.append(message_line)
        self.save()
    def delete(self):
        '''
        删
        '''
        class_student = input("input class:")
        ID_student = input("input ID:")
        name_student = input("input name:")
        self.get()
        flag = False
        for i in self.message_list:
            if i[0]==class_student and i[1]==ID_student and i[2]==name_student:
                self.message_list.remove(i)
                flag=True
        if flag:
            print('delete successful')
            self.save()  
        else:
            print('no found')
    def find(self):
        '''查'''
        class_student = input("input class:")
        ID_student = input("input ID:")
        name_student = input("input name:")
        self.get()
        flag = False
        for i in self.message_list:
            if i[0]==class_student and i[1]==ID_student and i[2]==name_student:
                message = i
                flag=True
        if flag:
            print('class:{}, ID:{}, name:{}, python score:{}'.format(message[0],message[1],message[2],message[3])) 
        else:
            print('no found')
    def update(self):
        class_student = input("input class:")
        ID_student = input("input ID:")
        name_student = input("input name:")
        self.get()
        flag = True
        for i in range(len(self.message_list)):
            if self.message_list[i][0]==class_student and self.message_list[i][1]==ID_student and self.message_list[i][2]==name_student:
                print('class:{}, ID:{}, name:{}, python score:{}'.format(self.message_list[i][0],self.message_list[i][1],self.message_list[i][2],self.message_list[i][3]))
                new_score = input('input new python score:')
                self.message_list[i][3] = new_score
                self.save()
                flag = False
        if flag:
            print('no found')
        
l=[['class1','123', 'tony', 99]]
m=python_score(l)
# print('增')
# m.add()

# print('删')
# m.delete()

# print('查')
# m.find()

print('改')
m.update()
