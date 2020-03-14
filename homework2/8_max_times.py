# -*- encoding: utf-8 -*-
'''
@File : 8_max_times.py
@Time : 2020/03/14 17:20:23
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib
'''
请用Python定义一个函数，给定一个字符串，
找出该字符串中出现次数最多的那个字符，并打印出该字符及其出现的次数。
 例如，输入 aaaabbc，输出：a:4
'''
def string_times(string):
    a = [i for i in string]
    words = set(a)
    b = {word:a.count(word) for word in words}
    times = 0
    for k,v in b.items():
        if v > times:
            times = v
            word = k
        
    print(word ,":",times)

if __name__ == "__main__":
    string = "123asdfbcasadc"
    string_times(string)