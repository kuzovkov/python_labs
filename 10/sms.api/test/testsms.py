#coding=utf-8
import smsru

cli = smsru.Client()
print cli.send("+79877171421", u"привет лунатикам")

