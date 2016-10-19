import httplib

host="www.yandex.ru"

#создание запроса с помощью объекта HTTP
h=httplib.HTTP(host)
h.putrequest('GET','/')
h.putheader('Host',host)
h.endheaders()

#получение и печать кода ответа, сообщение ответа и заголовков ответа
returncode, returnmsg, headers = h.getreply()
print returncode
print headers
print returnmsg

#создание запроса с помощью объекта HTTPConnection
h=httplib.HTTPConnection(host)
h.putrequest('GET','/')
h.putheader('Host',host)
h.endheaders()

#получение сохранение текста web-страницы в файл
response=h.getresponse()  
f=open('response.txt','w')
f.write(response.read())
f.close()


print "-"*40,"GET","-"*30

#GET запрос HTTP1.1
host="site1.loc"
h=httplib.HTTPConnection(host)
h.putrequest('GET','/test_request.php?name=sania&age=35','HTTP1.1')
h.putheader('Host',host)
h.putheader('Cookie','sania567890=!@#$%')
h.endheaders()
response=h.getresponse()  
f=open('get_response.txt','w')
f.write(response.read())
f.close()
f=open('get_response.txt','r')
print f.read()
f.close()

print "-"*40,"POST","-"*30

#POST запрос HTTP1.1
host="site1.loc"
h=httplib.HTTPConnection(host)
body="name=sania&age=35"
headers={'Host':host,'Content-type':'application/x-www-form-urlencoded',
         'Cookie':'sania2121212121=qwer1234'}
h.request('POST','/test_request.php',body,headers)
response=h.getresponse()
f=open('post_response.txt','w')
f.write(response.read())
f.close()
f=open('post_response.txt','r')
print f.read()
f.close()




