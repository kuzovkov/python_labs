#coding=utf-8
import urllib2
import urllib


proxy='217.12.62.194:8080'
#GET запрос HTTP1.1

sstring="антивирус касперского"
sstring=urllib.quote_plus(sstring)



host="http://firebit.org"
url=host+'/index.php?do=search&q='+sstring+'&type=simple'

req=urllib2.Request(url)
req.add_header('User-Agent','Opera/9.80 (Windows NT 5.1) Presto/2.12.388 Version/12.16')
req.add_header('Accept-Language','ru-RU,ru;q=0.9,en;q=0.8')
req.add_header('Accept-Encoding','')

try:
    res=urllib2.urlopen(req)
except Exception:
    print "no connect ",url
else:
    f=open('get_response_firebit.org.urllib2.html','w')
    f.write(res.read())
    f.close()
    f=open('get_response_firebit.org.urllib2.html','r')
    print f.read()
    f.close()








