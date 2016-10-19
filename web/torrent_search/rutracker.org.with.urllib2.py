import urllib2
import urllib



#POST запрос HTTP1.1
host="http://rutracker.org"
url=host+'/forum/tracker.php'
sstring='антивирус касперского'


req=urllib2.Request(url)

data=urllib.urlencode({'max':1,'nm':sstring})
req.add_header('Cookie','bb_data=1-24459730-qHzZY1vwsOqjvSuOHeX7-1294481547-1385280557-1385280557-2882093672-0; spylog_test=1')
req.add_data(data)
try:
    res=urllib2.urlopen(req)
except Exception:
    print "no connect ",url
else:
    f=open('post_rutracker.urllib2.html','w')
    f.write(res.read())
    f.close()
    f=open('post_rutracker.urllib2.html','r')
    print f.read()
    f.close()




