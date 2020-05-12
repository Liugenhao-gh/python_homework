

'''  针对我们给大家的2张表（学生表和班级表），做以下查询；（查询脚本放在一个文件中，创建一个SQL文件夹，放到这个里面，最有提交到代码仓库）
① 查询所有男生的姓名，年龄，所在班级名称；
② 查询所有查询编号小于4或没被删除的学生；
③ 查询姓黄并且“名”是一个字的学生；
④ 查询编号是1或3或8的学生
⑤ 查询编号为3至8的学生
⑥ 查询未删除男生信息，按年龄降序
⑦  查询女生的总数
⑧  查询学生的平均年龄
⑨ 分别统计性别为男/女的人年龄平均值
⑩ 按照性别来进行人员分组如下显示（group by + group_concat()）；
        | 男     | 彭于晏,刘德华,周杰伦,程坤,郭靖                                 |
	| 女     | 小明,小月月,黄蓉,王祖贤,刘亦菲,静香,周杰                        |
	| 中性   | 金星                                                       |
	| 保密   | 凤姐                                                       |
'''
import pymysql
conn = pymysql.connect(host='Localhost', user='root', passwd="lgh1519", db='test')
cur = conn.cursor()
# 1查询所有男生的姓名，年龄，所在班级名称；
print('1'+'='*30)
sql = 'SELECT * FROM students WHERE gender = \'男\''
cur.execute(sql)
for r in cur:
    print('name:{} ; age:{}, class:{}'.format(r[1],r[2],r[5]))
    print(r)

#  2查询所有查询编号小于4或没被删除的学生；
# print('2' + '=' * 30)
# sql = 'SELECT * FROM students WHERE id < 4 AND is_delete = 0'
# cur.execute(sql)
# for r in cur:
#     print(r)

# 3 查询姓黄并且“名”是一个字的学生；
# print('3' + '=' * 30)
# sql = "select * from students where name like \"黄_\""
# cur.execute(sql)
# for r in cur:
#     print(r)

# 4 查询编号是1或3或8的学生
# print('4' + '=' * 30)
# sql = 'SELECT * FROM students WHERE id in (1, 3, 8)'
# cur.execute(sql)
# for r in cur:
#     print(r)

# 5 查询编号为3至8的学生
# print('5' + '=' * 30)
# sql = 'SELECT * FROM students WHERE id between 3 and 8'
# cur.execute(sql)

# for r in cur:
#     print(r)
# 6 查询未删除男生信息，按年龄降序
# print('6' + '=' * 30)
# sql = 'SELECT * FROM students WHERE is_delete =0 and gender = \'男\' order by age'
# cur.execute(sql)

# for r in cur:
#     print(r)

# 7 查询女生的总数
# print('7' + '=' * 30)
# sql = 'SELECT count(*) FROM students '
# cur.execute(sql)
# # conn.commit()
# for r in cur:
#     print(r[0])

# 8查询学生的平均年龄
# print('8' + '=' * 30)
# sql = 'SELECT avg(age) FROM students '
# cur.execute(sql)
# # conn.commit()
# for r in cur:
#     print(r[0])

# 9分别统计性别为男/女的人年龄平均值
# print('9' + '=' * 30)
# sql = 'SELECT avg(age) FROM students WHERE gender=\'男\''
# cur.execute(sql)
# # conn.commit()
# for r in cur:
#     print('男平均年龄：{}'.format(r[0]))
# sql = 'SELECT avg(age) FROM students WHERE gender=\'女\''
# cur.execute(sql)
# # conn.commit()
# for r in cur:
#     print('女平均年龄：{}'.format(r[0]))

# 10 按照性别来进行人员分组如下显示（group by + group_concat()）
print('10' + '=' * 30)
sql = 'select gender,group_concat(name) from students group by gender'
cur.execute(sql)
# conn.commit()
for r in cur:
    print(r)
conn.commit()
cur.close()
conn.close()