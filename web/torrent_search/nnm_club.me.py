import httplib
import urllib

proxies = {'http': 'http://www.someproxy.com:3128'}
#filehandle = urllib.urlopen(some_url, proxies=proxies)

#POST запрос HTTP1.1
host="nnm-club.me"


sstring='бесплатные антивирусы'
sstring=urllib.quote_plus(sstring)


h=httplib.HTTPConnection(host)
body="f=-1&nm="+sstring
headers={'Host':host,'Content-type':'application/x-www-form-urlencoded'}
h.request('POST','/forum/tracker.php',body,headers)
response=h.getresponse()
f=open('post_response_nnm_club.html','w')
f.write(response.read())
f.close()
f=open('post_response_nnm_club.html','r')
print f.read()
f.close()




