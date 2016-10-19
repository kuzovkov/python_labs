import urllib

city='Yoshkar-Ola'
date='tomorrow'
key='3rcap79crb4b9r8phwvqpbud'
rformat='xml'
url='http://api.worldweatheronline.com/free/v1/weather.ashx?q='+city+'&format='+rformat+'&num_of_days=5&date='+date+'&key='+key

web=urllib.urlopen(url)
txt=web.read()
print txt
