import re

#список данных поиска
data_ls=[]
temp_ls=[]


t1_re=re.compile('<a href="/forum/viewtopic.*?</a>')
t2_re=re.compile('<.*?>')
t3_re=re.compile('&.*?;')

l1_re=re.compile('<a href="/forum/viewtopic.*?</a>')
l2_re=re.compile('<a href="')
l3_re=re.compile('">.*?</a>')

s1_re=re.compile('<a href="/forum/download.*?</a>')
s2_re=re.compile('<.*?>')
s3_re=None

d1_re=re.compile('\d{4}-\d{2}-\d{2}\s\d{1,2}:\d{1,2}')
d2_re=None
d3_re=None

filename="tempout.html"

try:
    f=open(filename,"r")
except IOError:
    print "can't open file ",filename
else:
    content=f.read().decode('cp1251')
    #выводим названия
    t_items=t1_re.findall(content)

    for t_item in t_items:
        if t2_re != None:
            t_item=t2_re.sub('',t_item)
            if t3_re != None:
                t_item=t3_re.sub('',t_item)
        print t_item+"   \n"
        temp_ls.append(t_item)
    t_items=temp_ls
    temp_ls=[]
    
    
    #выводим ссылки
    l_items=l1_re.findall(content)

    for l_item in l_items:
        if l2_re != None:
            l_item=l2_re.sub('',l_item)
            if l3_re != None:
                l_item=l3_re.sub('',l_item)
        print l_item+"   \n"
        temp_ls.append(l_item)
    l_items=temp_ls
    temp_ls=[]


    #выводим размер
    s_items=s1_re.findall(content)

    for s_item in s_items:
        if s2_re != None:
            s_item=s2_re.sub('',s_item)
            if s3_re != None:
                s_item=s3_re.sub('',s_item)
        print s_item+"   \n"
        temp_ls.append(s_item)
    s_items=temp_ls
    temp_ls=[]

    #выводим дату
    d_items=d1_re.findall(content)

    for d_item in d_items:
        if d2_re != None:
            d_item=d2_re.sub('',d_item)
            if d3_re != None:
                d_item=d3_re.sub('',d_item)
        print d_item+"   \n"
        temp_ls.append(d_item)
    d_items=temp_ls
    temp_ls=[]

    print "-"*60

    print len(t_items),len(l_items),len(s_items),len(d_items)
    
    for i in range(min(len(t_items),len(l_items),len(s_items),len(d_items))):
        print t_items[i]," | ",l_items[i]," | ",s_items[i]," | ",d_items[i],"\n\n"

    
