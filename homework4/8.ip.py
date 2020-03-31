# -*- encoding: utf-8 -*-
'''
@File : 8.ip.py
@Time : 2020/03/31 19:03:41
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib

from random import randint
def mk_ip_txt():
    ip = '172.25.254.'
    with open(r'test\homework4\ip.txt',"w") as f:
        for i in range(1200):
          f.write(ip+str(randint(1,255))+" ")

def read_ip():
    iplist = []
    with open(r'test\homework4\ip.txt',"r") as f:
        iplist = f.read().split()
    ipset = set(iplist)
    ipdir = {ip: iplist.count(ip) for ip in ipset}
    ipsort = list(ipdir.items())
    ipsort.sort(key= lambda x : x[1])
    ipsort.reverse()
    print(ipsort[:10])

if __name__ == "__main__":
    read_ip()