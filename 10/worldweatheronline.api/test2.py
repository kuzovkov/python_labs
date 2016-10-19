from pywwo import *

key='3rcap79crb4b9r8phwvqpbud'
place='Yoshkar-Ola'
date='tomorrow'
setKey(key, 'free')
w=LocalWeather(place,num_of_days=5,date=date)
print 'место '+str(w.data.request.query)
print 'прогноз на '+str(w.data.weather.date)
print 'температура '+str(w.data.weather.tempMinC)+' - '+str(w.data.weather.tempMaxC)+' C'
print 'скорость ветра '+str(int(w.data.weather.windspeedKmph)/3.6)+'м/с'
print 'дополнительно '+str(w.data.weather.weatherDesc)
