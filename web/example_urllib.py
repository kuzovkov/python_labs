import urllib

#������������� proxy
proxies = {'http': 'http://217.12.62.194:8080'}

url="http://nnm-club.me"
try:
    web=urllib.urlopen(url,proxies=proxies)
except IOError:
    print "�� ���� ������� ",url
else:
    print web.headers
    print "-"*60
    print web.read()
    

#GET ������ � �����������
params = urllib.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
f = urllib.urlopen("http://www.musi-cal.com/cgi-bin/query?%s" % params)
print f.read()

#POST ������ � �����������
params = urllib.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
f = urllib.urlopen("http://www.musi-cal.com/cgi-bin/query", params)
print f.read()


# ������ ����� ������
proxies = {'http': 'http://proxy.example.com:8080/'}
opener = urllib.FancyURLopener(proxies)
f = opener.open("http://www.python.org")
f.read()
