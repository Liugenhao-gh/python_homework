# -*- encoding: utf-8 -*-
'''
@File : 3_web_mp3.py
@Time : 2020/05/06 17:29:33
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib
'''给定一个网址（包含了优质的英语学习音频文件），http://www.listeningexpress.com/studioclassroom/ad/； 请大家写一个爬虫，将里面的英语节目MP3，都下载下来
这个程序可以运行，但是由于下载的MP3文件过大，就不再提交下载文件。'''
import requests
import wget
from  bs4 import BeautifulSoup
import re
from urllib.parse import quote
import os 
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.3',
    'Referer': 'http://www.listeningexpress.com/studioclassroom/ad/',
}
url = "http://www.listeningexpress.com/studioclassroom/ad/"

if not os.path.exists("homework7\download"):
  os.mkdir("homework7\download")
downpath=os.path.join(os.path.abspath(os.getcwd()),"homework7\download")

try:
    response = requests.get(url=url,headers= headers,timeout=5)
    text = response.text
    print (downpath)
except:
    print('无法连接{}'.format(url))
else:
    
    mp3_urls = re.findall(r'sc-[a-zA-Z0-9 -.]+\.mp3',text) 
    for mp3_url in mp3_urls:
        # 用wget下载
        download_url_2 = url+mp3_url
        response = requests.get(download_url)
        print('downloading {}'.format(mp3_url))
        wget.download(download_url, out=os.path.join(downpath, mp3_url))
        # 用requests下载
        # download_url = url+quote(mp3_url)
        # with open(downpath+'\\'+mp3_url, 'ab') as f:
        #     f.write(response.content)
        # print('{} is downloaded successfully'.format(mp3_url))
        
#     print('下载完成。')
# 经过以下代码测试，wget下载文件的url 不需要quote()编码
# download_url = 'http://www.listeningexpress.com/studioclassroom/ad/sc-ad%202020-05-04%20The%20Faroe%20Islands.mp3'
# download_url = 'http://www.listeningexpress.com/studioclassroom/ad/sc-ad 2020-05-04 The Faroe Islands.mp3'
# wget.download(download_url, out=os.path.join(downpath, '1.mp3'))

