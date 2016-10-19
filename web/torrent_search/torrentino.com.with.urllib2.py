import urllib2
import urllib


proxy='60.190.138.151:80'
#GET запрос HTTP1.1

sstring='антивирус касперского'

sstring=urllib.quote_plus(sstring)
host="http://www.torrentino.com"
url=host+'/search?search='+sstring
req=urllib2.Request(url)
req.set_proxy(proxy,'http')

try:
    res=urllib2.urlopen(req)
except Exception:
    print "no connect ",url
else:
    f=open('get_response_torrentino.com.urllib2.html','w')
    f.write(res.read())
    f.close()
    f=open('get_response_torrentino.com.urllib2.html','r')
    print f.read()
    f.close()








