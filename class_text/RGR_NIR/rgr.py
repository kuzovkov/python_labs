# -*- coding: utf-8 -*-

import re

tech = []
rep_tech = {}

xokkej = []
rep_xokkej = {}

f = open('Tech1.txt', 'r')
txt1 = f.read()

try:
    txt1=txt1.decode('utf8')
except UnicodeDecodeError:
    txt1=txt1.decode('cp1251')
    
#txt1 = txt1.encode('utf-8')
txt1 = txt1.replace("\n"," ")

# ubrat simvoli
p = re.compile('[^a-zA-Zа-яА-Я]')
txt1 = p.sub(" ",txt1)


words1 = txt1.split(" ")


for stroka in words1:
    if len(stroka) > 4:
        tech.append(stroka)

for stroka in tech:
    rep_tech[stroka] = tech.count(stroka)

# сортировка по значениям
rep2 = sorted(rep_tech.items(), key=lambda (k, v): v, reverse=True)

num = 20
if num > len(rep2):
    num = len(rep2)

for i in range(num):
    print "%2d: %s (%d)" %(i+1, rep2[i][0], rep2[i][1])

