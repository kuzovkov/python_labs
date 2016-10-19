#coding=cp1251
from test import *

print head
print "-"*60
print questions
print "-"*60
print variants
print "-"*60
print responses_str
print "-"*60
print responses_num
print "-"*60
print responses_or
print "-"*60
print responses_and

f=open('test.txt','r')
stroka=f.read()
f.close()
print stroka
print "*"*100

for i in range(1,len(questions)+1):
    print questions[i]

for i in range(1,len(variants)+1):
    print i
    for variant in variants[i]:
        print variant
    print "-----"
    print "ответ:"
    if responses_str.has_key(i):
        print responses_str[i]
    if responses_num.has_key(i):
        print responses_num[i]
    if responses_or.has_key(i):
        print responses_or[i]
    if responses_and.has_key(i):
        print responses_and[i]

    print "-"*60
    
