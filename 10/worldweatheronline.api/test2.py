from pywwo import *

key='3rcap79crb4b9r8phwvqpbud'
place='Yoshkar-Ola'
date='tomorrow'
setKey(key, 'free')
w=LocalWeather(place,num_of_days=5,date=date)
print '����� '+str(w.data.request.query)
print '������� �� '+str(w.data.weather.date)
print '����������� '+str(w.data.weather.tempMinC)+' - '+str(w.data.weather.tempMaxC)+' C'
print '�������� ����� '+str(int(w.data.weather.windspeedKmph)/3.6)+'�/�'
print '������������� '+str(w.data.weather.weatherDesc)
