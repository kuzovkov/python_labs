#coding=utf-8
import urllib2
import urllib


proxy='217.12.62.194:8080'
#GET запрос HTTP1.1

sstring='антивирус касперского'

sstring=urllib.quote_plus(sstring)

host="http://tfile.me"
url=host+'/forum/ssearch.php?q='+sstring
req=urllib2.Request(url)  

try:
    res=urllib2.urlopen(req)
except Exception:
    print "no connect ",url
else:
    f=open('get_response_tfile.urllib2.html','w')
    f.write(res.read())
    f.close()
    f=open('get_response_tfile.urllib2.html','r')
    print f.read()
    f.close()








