# -*- encoding: utf-8 -*-
'''
@File : 4_num_abc.py
@Time : 2020/03/12 12:44:32
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib
'''
写函数，统计字符串中有几个字母，几个数字，几个空格，几个其他字符，并返回结果;
'''
def num_abc(str):
    """ str is a string
     (a,b,c,d) a is number of letter. b is number of number. 
    c is number of blank. d is number of other.
    """
    a = 0
    b = 0
    c = 0
    d = 0
    for i in str:
        if i >= 'A' and i <= 'z':
            a += 1
        elif i>='0' and i<= '9':
            b += 1
        elif i == ' ':
            c += 1
        else:
            d += 1
    return a, b, c, d

if __name__ == "__main__":
    str = "abc123  .."
    print(num_abc(str))
