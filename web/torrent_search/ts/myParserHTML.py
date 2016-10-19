#coding=utf-8

import re
from HTMLParser import HTMLParser

result=[]

class MyHTMLParser(HTMLParser):
    def __init__(self,tag,attr,attrValue,encode,empty,attrOnly):
        global result
        self.flag_tag=False
        self.tag=tag
        self.attr=attr
        self.attrValue=attrValue
        self.count=0
        self.encode=encode
        self.empty=empty
        self.attrOnly=attrOnly
        self.sCut=['  ','   ','\n','\t','\v']
        result=[]
        HTMLParser.__init__(self)
        
    
    def handle_starttag(self, tag, attrs):
        global result
        if tag==self.tag:
            for attrib in attrs:
                if self.attrOnly:
                    if attrib[0]==self.attr and attrib[1].find(self.attrValue) != -1:
                        result.append(attrib[1])
                else:
                    if attrib[0]==self.attr and attrib[1]==self.attrValue:
                        self.flag_tag=True

            
    def handle_endtag(self, tag):
        if tag==self.tag and self.flag_tag:
            self.flag_tag=False
            
       

    def handle_data(self, data):
        global result
        if not self.attrOnly:
            if self.flag_tag:
                string=data.decode(self.encode)
                for char in self.sCut:
                    string=string.replace(char,'')
                if self.empty:
                    result.append(string)
                else:   
                    if string != '':
                        result.append(string)
        
'''
Получение данных тега или его атрибутов
Параметры       Default       Description
content           None          строка html контента
tag                'a'             тег
attr              'class'           название атрибута
attrValue           ''            значение атрибута
encode           'cp1251'         кодировка файла
start                0              с какого выводить из списка найденных
end                 END           до какого выводить в списке найденных   
step                 1            шаг вывода в списке найденных
attrOnly          False            вывод текста либо значения аттрибута
filename          False           имя распарсиваемого файла

'''

def findTagAttr(content=None,**keywords):
    tag=keywords.get('tag','a')
    attr=keywords.get('attr','class')
    attrValue=keywords.get('attrValue','')
    encode=keywords.get('encode','cp1251')
    empty=keywords.get('empty',False)
    start=keywords.get('start',0)
    end=keywords.get('end',0)
    step=keywords.get('step',1)
    attrOnly=keywords.get('attrOnly',False)
    filename=keywords.get('filename',False)


    if not filename and content == None:
        return False
    if filename:
        try:
            f=open(filename,"r")
        except IOError:
            return False
        else:
            content=f.read()
            f.close()
        
    #вырезаем с помощью рег. выр. ненужные теги
    
    reList=['</?em>','</?i>','</?i>','</?b>','</?br>','\s{2,}']
    for reItem in reList:
        reObj=re.compile(reItem)
        content=reObj.sub('',content)
    
    parser=MyHTMLParser(tag,attr,attrValue,encode,empty,attrOnly)
    parser.feed(content)
    if end == 0:
        end = len(result)
    return result[start:end:step]
    
    
