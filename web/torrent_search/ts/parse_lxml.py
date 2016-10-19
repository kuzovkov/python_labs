#парсинг html с помощью htql
#the best!!!
import lxml.html
import re

filename="temp.html"
content=open(filename,"r").read()

cutTag=re.compile('<.[^<>]*>')
cutSpace=re.compile('\s{2,}')


#titles,links
doc=lxml.html.document_fromstring(content)

resTitle=doc.find_class('genmed')

titles=[]

for item in resTitle:  
    title=item.get('text')
    #title=cutTag.sub('',title)
    #title=cutSpace.sub('',title)
    titles.append(title)

print len(titles)
for item in titles:
    print item

'''
#links
queryLink="<td INSEN (class='genmed')>.<a>:href"
resLink=htql.HTQL(content,queryLink)
links=[]
for link in resLink:
    link=cutTag.sub('',link)
    link=cutSpace.sub('',link)
    links.append(link)
      

#size

querySize="<td INSEN(class='gensmall')>:tx"
resSize=htql.HTQL(content,querySize)
sizes=[]
for size in resSize:
    size=cutTag.sub('',size)
    size=cutSpace.sub('',size)
    sizes.append(size)
sizes=sizes[0:len(sizes):3]    

#date
queryDate="<td INSEN(class='gensmall')>:tx"
resDate=htql.HTQL(content,queryDate)
dates=[]
for date in resDate:
    date=cutTag.sub('',date)
    date=cutSpace.sub('',date)
    dates.append(date)
dates=dates[2:len(dates):3]

#output

for ls in (titles,links,sizes,dates):
    print len(ls)
    for item in ls:
        print item        
'''

