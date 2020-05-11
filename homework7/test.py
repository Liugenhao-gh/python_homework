# -*- encoding: utf-8 -*-
'''
@File : test.py
@Time : 2020/04/29 20:15:48
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib

import requests
from lxml import etree

# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
# }
# params = {'wd':'中国'}
# # response = requests.get('https://www.baidu.com',headers= headers)

# with open('baidu.html','w',encoding= 'utf-8') as fp:
#     fp.write(response.content.decode('utf-8'))

# print(response.cookies)
# print(response.status_code)

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Referer':'https://movie.douban.com/'
}
url = 'https://movie.douban.com/cinema/nowplaying/beijing/'

response = requests.get(url, headers=headers)
text = response.text
print(text)