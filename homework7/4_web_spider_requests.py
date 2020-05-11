# -*- encoding: utf-8 -*-
'''
@File : 4_web_spider_requests.py
@Time : 2020/05/07 19:45:32
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib
'''爬取这个网址上https://www.programcreek.com/python/，搜索request的范例代码；保存到txt文件中（只保留文字）；'''
import requests
from bs4 import BeautifulSoup
url = 'https://www.programcreek.com/python/example/3765/requests.get'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}

def get_html(url, headers):
    try:
        response = requests.get(url=url, headers=headers,timeout=5)
        html = response.content.decode('utf-8')
    except Exception as e:
        print(e)
    finally:

        return html


def get_message(html):
    soup = BeautifulSoup(html,'lxml')
    pres = soup.find_all('pre')
    return pres

def save_in_txt(pres):
    with open(r'C:/Git/Github/python_homework/homework7/example_requests_get.txt', 'w', encoding='utf-8') as f:
        for pre in pres:
            f.write('='*40+'\n')
            f.write(pre.string)
            f.write('\n')

if __name__ == '__main__':
    html = get_html(url,headers)
    pres = get_message(html)
    save_in_txt(pres)