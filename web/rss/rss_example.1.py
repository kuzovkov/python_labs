#coding=utf-8
#рассылка на email новостей в формате RSS с сайта lenta.ru
import urllib
import smtplib
from email.mime.text import MIMEText

url="http://lenta.ru/rss"
filename="lenta.ru.rss.xml"
me = 'dionis20095@mail.ru'
you = 'dionis20095@rambler.ru'
smtp_server = 'smtp.mail.ru'

try:
    rss=urllib.urlopen(url)
except IOError:
    print "не могу открыть ",url
else:
    try:
        f_rss=open(filename,"w")
    except IOError:
        print "не могу открыть ",filename
    else:
        f_rss.write(rss.read())
        f_rss.close()

        f_rss=open(filename,"r")
        rss_str=f_rss.read()
        f_rss.close()
        print rss_str

        msg = MIMEText(rss_str)
        msg['Subject'] = 'RSS lelta.ru'
        msg['From'] = me
        msg['To'] = you
        s = smtplib.SMTP(smtp_server)
        s.login('dionis20095@mail.ru','sania229497')
        s.sendmail(me, you, msg.as_string())
        s.quit()
        
        
    
