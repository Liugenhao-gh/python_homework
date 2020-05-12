# -*- encoding: utf-8 -*-
'''
@File : mysql.py
@Time : 2020/05/08 07:57:37
@Author : xdbcb8
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib
'''创建一个留言板的表（ID，留言主题，留言人，留言时间）4个字段，注意，字段请用英文；
   完成对这个表记录的增，删，改，查询；
   用PyMySQL驱动方式'''
import pymysql
conn = pymysql.connect(host='Localhost', user='root', passwd="lgh1519", db='test')
cur = conn.cursor()
# cur.execute("SELECT * FROM user")
# for r in cur:
#   print(r)
# 增
sql="INSERT INTO user(id,theme,name) VALUES (2,'study','amy');"
cur.execute(sql)
print(sql)
conn.commit()
# 删
# sql="delete from user where id =1 "
# cur.execute(sql)
# 改
# sql="update user set time='6:00' where id=2"
# cur.execute(sql)
# 查
# sql="select * from user where id =3"
# cur.execute(sql)
# for r in cur:
#       print(r)
# conn.commit()
# cur.execute("SELECT * FROM user")
# for r in cur:
#   print(r)
cur.close()
conn.close()
# print('hello')