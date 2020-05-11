# -*- encoding: utf-8 -*-
'''
@File : 2_spider.py
@Time : 2020/04/19 18:07:49
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib

'''给定100个企业网站首页链接地址（用1中给出的URL地址）；请爬取每个页面上，企业介绍的链接地址；
    说明，满足企业介绍网址的条件是， 标题包含：企业介绍，关于我们，企业发展，发展历史，企业概况等关键字的URL地址；
    提示：要用到requests库，BeautifulSoup库'''

import requests
from bs4 import BeautifulSoup  
import re
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',}


with open(r'homework7\webUrl.txt', 'r', encoding='utf-8') as f:
    urls = f.readlines()

URL_compony = []
for url in urls[0:100]:
    url = url.strip()
    try:
        # print('访问{}'.format(url))
        response = requests.get(url=url, headers= headers,timeout=5)
        text = response.content.decode('utf-8')
    except:
        print('连接失败{}'.format(url))
    else:
        soup = BeautifulSoup(text,'lxml')
        aList = soup.find_all('a')
        for a in aList:
            if re.search(r'(企业介绍)|(关于我们)|(企业发展)|(发展历史)|(企业概况)', a.text):

                # print(a.text)
                try:
                    URL_compony.append(url+'/'+a.attrs['href']+'/\n')
                except KeyError as e:
                    print(e)
                # print(url+'/'+a.attrs['href']+'/')

with open(r"homework7\compony_URL.txt",'w', encoding='utf-8') as f:
    f.writelines(URL_compony)
