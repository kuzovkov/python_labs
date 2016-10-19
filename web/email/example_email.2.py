import smtplib   
from email.mime.text import MIMEText    
me = 'dionis20095@mail.ru'
you = 'dionis20095@rambler.ru'
smtp_server = 'smtp.mail.ru'
msg = MIMEText('Hello from Python!!! \n Привет от питона!!!')
msg['Subject'] = 'Привет от Питона!'
msg['From'] = me
msg['To'] = you
s = smtplib.SMTP(smtp_server)
s.login('dionis20095@mail.ru','sania229497')
s.sendmail(me, you, msg.as_string())
s.quit()
