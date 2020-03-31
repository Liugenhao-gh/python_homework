# -*- encoding: utf-8 -*-
'''
@File : 3.account_password.py
@Time : 2020/03/31 16:43:34
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib

counter = 1
name = []
account = []
password = []
while counter <= 5:
    name.append(input("名字："))
    account.append(input("账号："))
    password.append(input("密码："))
    counter += 1

import hashlib
md5_password = []

for psw in password:
    md5 = hashlib.md5()
    md5.update(psw.encode("utf-8"))
    md5_password.append(md5.hexdigest())
with open(r"test\homework4\account&password.txt", "w",encoding="utf-8") as f:
    for i in range(len(name)):
        f.write(name[i]+"\t"+account[i]+"\t"+md5_password[i]+"\n")