# -*- encoding: utf-8 -*-
'''
@File : 3.py
@Time : 2020/03/20 17:38:45
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib

'''
3 编写一个程序，读取文件中保存的10个学生成绩名单信息
(学号,姓名, Python课程分数);
 然后按照分数从高到低进行排序输出
'''
score = []
with open(r"test\homework3\score.txt", "r", encoding='utf-8') as f:
    for line in f.readlines():
        score.append(line.split())
head = score[0]
score = score[1:]
score.sort(key = lambda x : x[2])
score.reverse()
print(head[0],'\t',head[1],'\t',head[2])
for item in score:
    print(item[0],'\t',item[1],'\t',item[2])
