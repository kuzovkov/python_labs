#парсинг с помощью моего модуля myParserHTML
import myParserHTML

filename='test.html'

f=open(filename,'rb')

content=f.read()


#rows
ls_result=myParserHTML.findTagAttr(content,tag='td',attr='class',attrValue='col2')
print len(ls_result)
for item in ls_result:
    print item

#titles
ls_result=myParserHTML.findTagAttr(content,tag='td',attr='class',attrValue='t')
print len(ls_result)

for item in ls_result:
    print item

#links
ls_result=myParserHTML.findTagAttr(filename=filename,tag='a',attr='href',attrValue='/forum/viewtopic.php',attrOnly=True)
print len(ls_result)

for item in ls_result:
    print item

#size
ls_result=myParserHTML.findTagAttr(filename=filename,tag='td',attr='class',attrValue='dl',step=1,empty=True)
print len(ls_result)

for item in ls_result:
    print item


#date
ls_result=myParserHTML.findTagAttr(content,tag='td',attr='class',attrValue='ms')
print len(ls_result)

for item in ls_result:
    print item


