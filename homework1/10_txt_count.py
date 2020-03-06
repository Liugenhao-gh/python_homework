# -*- encoding: utf-8 -*-
'''
@File : 10_txt_count.py
@Time : 2020/03/06 18:49:24
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib

test = "Live my life free of compromise and step into the shadow without complaint or regret. of and  my "
txt = test.split()
print(txt)
counter = {}
for i in txt:
    for k, v in counter.items():
        if k == i:         
            counter[k] = v+1
            break
    else:
        counter[i] = 1
print(counter)
