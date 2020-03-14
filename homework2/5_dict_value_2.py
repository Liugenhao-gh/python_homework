# -*- encoding: utf-8 -*-
'''
@File : 5_dict_value_3.py
@Time : 2020/03/13 18:51:10
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib
'''
写函数，检查传入字典的每一个value长度，如果大于2，
那么仅保留前两个长度的内容，并将新内容返回给调用者;
'''
def  dict_value_2(dict1):
    dict2 = {}
    for k, v in dict1.items():
        if len(v)>2:
            dict2[k] = v[0:2]
        else:
            dict2[k] = v
    return dict2
if __name__ == "__main__":
    dict1 = {
        1: "123",
        2: "456",
        3: "78",
        4: "9"
    }
    print(dict_value_2(dict1))


