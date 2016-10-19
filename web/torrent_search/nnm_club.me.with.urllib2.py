import urllib2
import urllib

#использование прокси сервера если сайт заблокирован
proxy = '217.12.62.194:8080'

#POST запрос HTTP1.1
host="http://nnm-club.me"
url=host+'/forum/tracker.php'
sstring='windows 8'
data=urllib.urlencode({'f':-1,'nm':sstring})

req=urllib2.Request(url)
req.add_data(data)
#req.set_proxy(proxy,'http')

try:
    res=urllib2.urlopen(req)
except Exception:
    print "no connect ",url
else:
    
    f=open('post_response_nnm_club.urllib2.html','w')
    f.write(res.read())
    f.close()
    f=open('post_response_nnm_club.urllib2.html','r')
    print f.read()
    f.close()




