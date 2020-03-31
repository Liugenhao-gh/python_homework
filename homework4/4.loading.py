# -*- encoding: utf-8 -*-
'''
@File : 4.loading.py
@Time : 2020/03/31 17:06:07
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib
import hashlib
name = []
account = []
password = []
with open(r"test\homework4\account&password.txt","r") as f:
    for line in f.readlines():
        info = line.split()
        name.append(info[0])
        account.append(info[1])
        password.append(info[2])
counter = 3
while counter >= 1:
    user = input("请输入名字：")
    if user in name:
        index = name.index(user)
        user_account = input("请输入账号：")
        if user_account == account[index]:
            user_password = input("请输入密码：")
            md5 = hashlib.md5()
            md5.update(user_password.encode("utf-8"))
            if md5.hexdigest() == password[index]:
                print("登录成功！")
                counter = 0
            else:
                counter -= 1
                print("密码错误，登录失败，还有{}次机会，请重试".format(counter))
        else:
            counter -= 1
            print("账号错误，登录失败，还有{}次机会，请重试".format(counter))

    else:
        counter -=1
        print("没有这个名字，登录失败，还有{}次机会，请重试".format(counter))