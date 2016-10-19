#парсинг html с помощью htql
#the best!!!
import htql
import re

filename="temp.html"
content=open(filename,"r").read()

#boundary="forumline tablesorter"
#content=content[content.find(boundary)::]

cutTag=re.compile('<.[^<>]*>')
cutSpace=re.compile('\s{2,}')
cutSpace2=re.compile('&nbsp;')
cutU=re.compile('<u>.[^<>]*</u>')
cutCod=re.compile('&#\d{1,};')

#print content

#titles
queryTitle="<tr INSEN (class='gai' or class='tum')>.<td>2.<a>2:tx"
resTitle=htql.HTQL(content,queryTitle)

titles=[]

for title in resTitle:  
    title=cutTag.sub('',title)
    title=cutSpace.sub('',title)
    titles.append(title)
    


#links
queryLink="<tr INSEN (class='gai' or class='tum')>.<td>2.<a>2:href"
resLink=htql.HTQL(content,queryLink)
links=[]
for link in resLink:
    link=cutTag.sub('',link)
    link=cutSpace.sub('',link)
    links.append(link)
      

#size  

querySize="<tr INSEN (class='gai' or class='tum')>.<td>3:tx"
resSize=htql.HTQL(content,querySize)
sizes=[]
for size in resSize:
    size=cutU.sub('',size)
    size=cutCod.sub('',size)
    size=cutTag.sub('',size)
    size=cutSpace.sub('',size)
    size=cutSpace2.sub(' ',size)
    sizes.append(size)
sizes=sizes[0:len(sizes):1]    

#date
queryDate="<tr INSEN (class='gai' or class='tum')>.<td>1:tx"
resDate=htql.HTQL(content,queryDate)
dates=[]
for date in resDate:
    date=cutU.sub('',date)
    date=cutTag.sub('',date)
    date=cutSpace.sub('',date)
    dates.append(date)
dates=dates[0:len(dates):1]

#output

for ls in (titles,links,sizes,dates):
    print len(ls)
    for item in ls:
        print item        


