# -*- encoding: utf-8 -*-
'''
@File : 6_Fibonacci_def.py
@Time : 2020/03/14 16:54:16
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib
'''
定义一个函数, 打印输出n以内的斐波那契数列;
'''
def Fibonacci(n):
    f1 = 0
    f2 = 1
    f3 = 1
    print(f1,f2,end=" ")
    while(f1+ f2 <=n):
        f3 = f1 +f2
        print(f3, end=" ")
        f1 = f2
        f2 = f3
    
if __name__ == "__main__":
    Fibonacci(5)