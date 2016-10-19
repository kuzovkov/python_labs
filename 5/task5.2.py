#�������� ��������� ������������
import urllib
import re

url=raw_input("������� URL: ")

tag=re.compile('<.[^<>]*>')
script=re.compile('<script.[^<>]*>.*</script>')
fig=re.compile('{.*}')
space=re.compile('[ ]{2,}')
numeric=re.compile('[0-9#$&]')

#url="http://www.rambler.ru"


try:
    web=urllib.urlopen(url)
   
    
except IOError:
    print "�� ���� ������� ��������",url
else:
    txt=web.read()
    
    ftemp=open("temp.txt","wb")
    ftemp.write(txt)
    ftemp.close()
    web.close()
    ftemp=open("temp.txt","rb")
    
    stroka=ftemp.read()
    
    ftemp.close()

    #����������� � �����������
    
    try:
        
        stroka=stroka.decode('utf8')
    except UnicodeDecodeError:
        stroka=stroka.decode('cp1251')

    #������ �����

    stroka=script.sub(" ",stroka) #javascript
    stroka=tag.sub(" ",stroka) #tags
    stroka=fig.sub(" ",stroka)  #{}
    stroka=space.sub(" ",stroka)
    
    stroka=stroka.replace("-\n","")
    filter_null=[".",",","-","_","(",")","\"","\'",":","!","=","?","+","$","{","}",";"]
    filter_space=[" - ","  ","   ","     ","\n","\t","&nbsp","&qt"]
    for ch in filter_space:
        stroka=stroka.replace(ch," ")

    for ch in filter_null:
        stroka=stroka.replace(ch,"")

    stroka=numeric.sub("",stroka)

    '''
    tf=open("tp.txt","wb")
    try:
        stroka=stroka.encode('utf8')
        tf.write(stroka)
        tf.close()
    except UnicodeDecodeError:
        stroka=stroka.encode('cp1251')
        tf.write(stroka)
        tf.close()
    '''
    #print stroka

        
    d={}
    #����� �� �����
    ls_str=stroka.split()
    #������������ �����
    for word in ls_str:
        if d.has_key(word):
            d[word]=d[word]+1
        else:
            d.update({word:1})

    
    #������� ���� � ���������� ��������   
    frq=d.values()
    frq=list(set(frq))
    frq.sort(reverse=True)
    frq=frq[0:5]
    

    print "�������� ����� ������������� 5 ���� � web-�������� ",url,":"
    for i in frq:
        for word,key in d.items():
            if key==i:
                print word,"-",key
    
    
    
  
    

