import urllib
import urllib2

sstring="бесплатный антивирус"
host="http://site1.loc//test_request.php"
proxies = {'http': 'http://217.12.62.194:8080'}
data=urllib.urlencode({'f':'-1','nm':sstring})


print "-"*40,"POST","-"*40

#POST запрос
req=urllib2.Request(url=host)
req.add_header('Cookie','87654342bgrvtfew=234567')
req.add_data(data)
#req.set_proxy('http://217.12.62.194:8080','http')

try:
    web=urllib2.urlopen(req)
except Exception:
    print "no connect ",host
else:   
    print web.read()


print "-"*40,"GET","-"*40

#GET запрос

host2=host+"?name=sania&age=35"
req2=urllib2.Request(url=host2)
req2.add_header('Cookie','87654342bgrvtfew=12qwerftgh')
try:
    web=urllib2.urlopen(req2)
except Exception:
    print "no connect ",host2
else:
    print web.read()


