#coding=utf-8
from pywwo import *
import smsru

key='3rcap79crb4b9r8phwvqpbud' #ключ сервиса Weather Service  
date='tomorrow' #запрашиваемый интервал
clients='clients.txt' #файл с номерами телефонов и названиями населенных пунктов

desc_ru={'Mist':'Туман','Rain':'Дождь','Snow':'Снег',
    'Light snow':'Небольшой снег','Light rain':'Небольшой дождь',
    'Hail':'Град','Cloudy':'Облачно','Sunny':'Солнечно'}


city={'Yoshkar-Ola':'Йошкар-Ола','Moscow':'Москва','London':'Лондон','Tokyo':'Токио'}
country={'Russia':'Россия','United Kingdom':'Великобритания','Japan':'Япония'}

setKey(key, 'free')
cli = smsru.Client()

f=open(clients,'r')
data=f.read()
f.close()

rows=data.split('\n')
abonents=[]
for row in rows:
    abonents.append(row.split(','))

def getWeather(place,date='tomorrow'): #формирование строки с прогнозом
    global city,country,desc_ru
    w=LocalWeather(place,num_of_days=5,date=date)
    ls=str(w.data.request.query).split(', ')
    strana=ls[1]
    gorod=ls[0]
    place1=city.get(gorod,gorod)
    place2=country.get(strana,strana)
    string=(u''+str(place1+', '+place2).decode('utf8'))
    string+=(u'\n'+str(w.data.weather.date))
    string+=(u'\nT '+str(w.data.weather.tempMinC)+' - '+str(w.data.weather.tempMaxC)+' C')
    string+=(u'\V ветра '+str(int(float(w.data.weather.windspeedKmph)/3.6))+u' м/с')
    desc=desc_ru.get(w.data.weather.weatherDesc,w.data.weather.weatherDesc)
    string+=(u'\n'+str(desc).decode('utf8'))
    return string


for abonent in abonents:
    print cli.send(abonent[0], getWeather(abonent[1]))

