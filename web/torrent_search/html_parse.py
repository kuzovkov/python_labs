#coding=utf-8
'''
'''
from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        self.flag_h3=False
        self.flag_a=False
        HTMLParser.__init__(self)
        
    
    def handle_starttag(self, tag, attrs):
        if tag=='a':
            for attr in attrs:
                if attr[0]=='class' and attr[1]=='light-link':
                    self.flag_a=True
            if self.flag_a:
                for attr in attrs:
                    if attr[0]=='href':
                        print attr[1]
                    
        elif tag=='h3':
            for attr in attrs:
                if attr[0]=='class' and attr[1]=='result__title':
                    self.flag_h3=True
                    #print "<",tag,">"
            
    def handle_endtag(self, tag):
        if tag=='h3' and self.flag_h3:
            #print "</",tag,">"
            self.flag_h3=False
        if tag=='a' and self.flag_a:
            #print "</",tag,">"
            self.flag_a=False

    def handle_data(self, data):
        if self.flag_h3:
            print data.decode('utf8')
        

filename="get_response_tfile.urllib2.html"
attrib=[('class','result__title')]
try:
    f=open(filename,"r")
except IOError:
    print "can't open file ",filename
else:
    content=f.read()
    parser=MyHTMLParser()
    parser.feed(content)
    
