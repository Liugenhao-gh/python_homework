# -*- encoding: utf-8 -*-
'''
@File : 10_caculate.py
@Time : 2020/03/14 17:48:21
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib

'''
编写一个函数cacluate, 
可以实现2个数的运算(加,减 乘,除)
'''
def caculate(a,b,sign):
    if sign =='+':
        return a+b
    elif sign == '-':
        return a-b
    elif sign == '*':
        return a*b
    elif sign == '/':
        if b==0:
            return "被除数不能为零！"
        else:
            return a/b
    
if __name__ == "__main__":
    print(caculate(1,3,'*'))