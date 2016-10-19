import httplib
import urllib

print "-"*40,"GET","-"*30

#GET запрос HTTP1.1

sstring='скачать windows 8'

sstring=urllib.quote(sstring)

host="tfile.me"
h=httplib.HTTPConnection(host)
h.putrequest('GET','/forum/ssearch.php?q='+sstring,'HTTP1.1')
h.putheader('Host',host)
#h.putheader('Cookie','sania567890')
h.endheaders()
response=h.getresponse()  
f=open('get_response_tfile.html','w')
f.write(response.read())
f.close()
f=open('get_response_tfile.html','r')
print f.read()
f.close()








