import httplib
import urllib



#POST запрос HTTP1.1
host="rutracker.org"
sstring='бесплатный антивирус'

sstring=urllib.quote_plus(sstring)

h=httplib.HTTPConnection(host)
body="f=-1&nm="+sstring
headers={'Host':host,'Content-type':'application/x-www-form-urlencoded',
         'Cookie':'bb_data=1-24459730-IwYLGOVsrRmYo0eqySF1-1294481547-1383735528-1383735528-654679495-0; spylog_test=1'}
h.request('POST','/forum/tracker.php',body,headers)
response=h.getresponse()
f=open('post_rutracker.html','w')
f.write(response.read())
f.close()
f=open('post_rutracker.html','r')
print f.read()
f.close()




