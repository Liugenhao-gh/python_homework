# -*- encoding: utf-8 -*-
'''
@File : 1_URL.py
@Time : 2020/04/19 17:04:33
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''
'''给定一个文件，请用正则表达式，逐行匹配提取其中的URL链接信息，并保存到另外一个文件中；
   提示，文件有1000行，注意控制每次读取的行数；'''
# here put the import lib
import re
with open(r"homework7\webspiderUrl.txt", 'r', encoding = 'utf-8') as f:
    urllist = f.readlines()

with open(r"homework7\webUrl.txt", 'w', encoding='utf-8') as f:
    for l in urllist:
        ret = re.search(r"(http://.+)\'\)\;$", l)
        if ret:
            f.write(ret.group(1).split(';')[0]+"\n")
        else:
            print("no search {}".format(l))


