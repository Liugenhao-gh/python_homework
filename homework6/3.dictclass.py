# -*- encoding: utf-8 -*-
'''
@File : 3.dictclass.py
@Time : 2020/04/14 19:41:47
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib
'''定义一个字典类：dictclass。完成下面的功能：
dict = dictclass({你需要操作的字典对象})
1 删除某个key
del_dict(key)
2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"
get_dict(key)
3 返回键组成的列表：返回类型;(list)
get_key()
4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)
update_dict({要合并的字典})'''

class dictclass:
    def __init__(self, dictionary):
        self.dictionary = dictionary
    def del_dict(self, key):
        del self.dictionary[key]
    def get_dict(self, key):
        if key in self.dictionary:
            return self.dictionary[key]
        else:
            return "not found"
    def get_key(self):
        key = self.dictionary.keys()
        return key
    def update_dict(self, dictionary):
        self.dictionary.update(dictionary)
        return self.dictionary
dictionary = dictclass({'1':1, '2':2})
dictionary.del_dict('1')
print(dictionary.get_dict('1'))
print(dictionary.get_dict('2'))
print(dictionary.update_dict({'3':3}))
