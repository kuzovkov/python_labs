#Кузовков Александр Владимирович

ls1=range(1,10)

#1
print "#1"
print "возведение чисел в третью степень"
print ls1
print map(lambda x:x*x*x,ls1)

print "-"*60

#2
print "#2"
print "вывод длины слов списка"
ls2=["wqwq","212nkjmklkl","smkwsk","qwqwsqws"]
print ls2
print dict(zip(ls2,map(lambda x:len(x),ls2)))

print "-"*60

#3
print "#3"
print "функция, возвращающую функцию, возводящую число в заданную степень"
funct=lambda x:x*x*x
n=5
print "куб числа ",n,"= ",funct(5)

print "-"*60

#4
print "#4"
print "словарь с lambda фунциями"
funct1=lambda x: x-1
funct2=lambda x: x+1
funct3=lambda x: -x
funct4=lambda x: x*x


d={'dec':funct1,'inc':funct2,'neg':funct3,'sq':funct4}

print "n= ",n
print "декремент ",n,"= ",d['dec'](n)
print "инкремент ",n,"= ",d['inc'](n)
print "обратное ",n,"= ",d['neg'](n)
print "квадрат ",n,"= ",d['sq'](n)




