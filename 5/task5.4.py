#Кузовков Александр Владимирович
import urllib
import re

url=raw_input("Введите URL: ")

repl=re.compile('\n\t\s')
glink=re.compile('(<a (?=.*http).[^<>]*>.[^(<a>)(</a>)]*</a>)')
llink=re.compile('(<a (?!.*(http|javascript|mailto)).[^<>]*>.[^(<a>)(</a>)]*</a>)')



#url="http://www.yandex.ru"

file_l="local_links.html"
file_g="global_links.html"

fg=open(file_g,"w")
fl=open(file_l,"w")

try:
    web=urllib.urlopen(url)
except IOError:
    print "Не могу открыть URL"
else:

    stroka=web.read()
    web.close()
        
    #удаляем лишние пробелы
    stroka=repl.sub("",stroka)

    #global links
    ls_gl=glink.findall(stroka)
   
    #local links
        
    ls_loc=llink.findall(stroka)
    
    
    #print ls_loc
    header1="<h1>Global Links Page &nbsp"+url+":</h1>\n"
    header2="<h1>Local Links Page &nbsp"+url+":</h1>\n"
    fg.write(header1)
    for ag in ls_gl:
        fg.write(ag+"\n\n<br>")

    fl.write(header2)
    for al in ls_loc:
        fl.write(al[0]+"\n\n<br>")

    fg.close()
    fl.close()

    print "Завершено (См. файлы global_links.html, local_links.html)"
