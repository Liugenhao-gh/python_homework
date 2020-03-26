# -*- encoding: utf-8 -*-
'''
@File : 6.py
@Time : 2020/03/24 19:10:08
@Author : xdbcb8 
@Version : 1.0
@Contact : 838025538@qq.com
'''

# here put the import lib
def getTlist(txtfile):
    text = txtfile.read()
    for i in '!"#$%&()*+,-./;:<=>?@[\\]^‘_{|}~\'':
        text = text.replace(i,' ')
    tlist = text.split()
    return tlist

def get_words_frequency(tlist):
    tset = set(tlist)
    tdict = {word : tlist.count(word) for word in tset}
    return tdict

with open(r"test\homework3\EnglishText1.txt","r",encoding="utf-8") as f:
    tlist1 = getTlist(f)
    tdict1 = get_words_frequency(tlist1)
    frequency1 = list(tdict1.items())
    frequency1.sort(key = lambda x: x[1], reverse=True)
with open(r"test\homework3\words_frequency1.txt","w") as f:
    for line in frequency1:
        f.write(line[0]+"\t"+str(line[1]))
with open(r"test\homework3\EnglishText2.txt","r",encoding="utf-8") as f:
    tlist2 = getTlist(f)
    tdict2 = get_words_frequency(tlist2)
    frequency2 = list(tdict2.items())
    frequency2.sort(key = lambda x: x[1], reverse=True)
with open(r"test\homework3\words_frequency2.txt","w") as f:
    for line in frequency2:
        f.write(line[0]+"\t"+str(line[1]))
ten1 =[i[0] for i in frequency1[0:10]]
ten2 =[i[0] for i in frequency2[0:10]]
counter = 0
for word in ten1:
    if word in ten2:
        counter += 1
print("相似度：{}%".format(counter/10*100))