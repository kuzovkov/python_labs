#coding=utf-8
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.Header import make_header
from email.Utils import formatdate
import os
 
# параметры почтового сервера
server = 'smtp.mail.ru'
port = 25
# кодировка письма
icharset = 'utf-8'
 
def sendmail(to, subject, message):
    # данные авторизации
    username = 'dionis20095@mail.ru'
    password = 'sania229497'
 
    ### генерация передаваемого содобщения
    msg = MIMEMultipart()
     
    # заголовок
    hdr = make_header([(subject, icharset)])
    # параметры письма (отправитель, получатель, дата, тема письма
    msg['From'] = username
    msg['To'] = to
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = hdr
    # добавление к содержимому текста сообщения
    msg.attach(MIMEText(message, _charset=icharset))
     
    ### передача сообщения
    # установка соединения
    srv = smtplib.SMTP(server, port)
    srv.ehlo()
    # запуск шифрования (SSL соединение)
    srv.starttls()
    srv.ehlo()
    # авторизация
    srv.login(username, password)
    # передача сообщения
    srv.sendmail(username, to, msg.as_string())
    # завершение соединения
    srv.close()


sendmail('dionis20095@rambler.ru','hello Python','hello! message from python!!!\n Привет от Питона')
