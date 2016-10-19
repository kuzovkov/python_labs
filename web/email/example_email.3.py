#coding=utf-8
import smtplib
def mail(sender, subject, message, to):
    smtp_server = 'smtp.mail.ru'
    smtp_port = 25
    smtp_pasword = 'sania229497'
    mail_lib = smtplib.SMTP(smtp_server, smtp_port)
    mail_lib.login(sender, smtp_pasword)
    # В случае если функции передан не список с получателями
    # а обычную строку
    if not isinstance(to, str):
        to = ','.join(to)
    msg = 'From: %s\r\nTo: %s\r\nContent-Type: text/plain; charset="utf-8"\r\nSubject: %s\r\n\r\n' % (sender, to, subject)
    msg += message
    mail_lib.sendmail(sender, to, msg)
# отправляем письмо
message = "Привет из Python!!!!!"
mail('dionis20095@mail.ru', 'привет от Питона!!!', message, 'dionis20095@rambler.ru')
