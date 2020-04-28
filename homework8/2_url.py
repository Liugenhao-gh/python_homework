# -*- encoding: utf-8 -*-
'''
@File : 2_url.py
@Time : 2020/04/27 20:38:42
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib
'''给定一组数据网址数据，请判断这些网址是否可以访问； 用多线程的方式来实现；
   请查资料，Python的 requests库，如何判断一个网址可以访问；'''
import requests
from concurrent.futures import ThreadPoolExecutor

def url_is_good(url):

    r=requests.get(url,timeout=5)
    code = r.status_code

    if code == 200:
        print ('OK 网站访问正常'+ url)
    else:
        print  ("error"+url)

if __name__ == '__main__':
    with open(r'homework8\url_data.txt','r', encoding='utf-8') as f:
        all_url = f.readlines()
    
    executor = ThreadPoolExecutor(max_workers= 5)
    for i in all_url:
        urls = i.split('; ' or '\n')
        for url in urls:
            executor.submit(url_is_good,url)
# url='http://www.baidu.com'

# r=requests.get(url,timeout=5)

# code = r.status_code

# if code == 200:
#     print ('OK 网站访问正常')
# else:
#     print  ("error"+url)