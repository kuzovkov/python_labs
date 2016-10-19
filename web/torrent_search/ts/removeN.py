#проба удаления символов перевода строк из файла
filename='temp.html'
filenameOut='tempout.html'

f=open(filename,'r')
content=f.read()
f.close

#операции с контентом
content=content.replace('\n','')
content=content.replace('\t','')
content=content.replace('\v','')

f=open(filenameOut,'w')
f.write(content)
f.close


