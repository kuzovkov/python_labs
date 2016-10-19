#Кузовков Александр Владимирович
#итеративный метод
def fact_1(n):
    n=int(n)
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

#рекурсивный метод
def fact_2(n):
    if n>1:
        return n*fact_2(n-1)
    else:
        return 1


#через reduce
def fact_3(n):
    def mul(x,y):
        return x*y
    
    ls=range(1,n+1)
    return reduce(mul,ls)
    
    
        
    


#Проверка
#1
print "итеративный метод"
for x in range(1,6):
    print "fact_1(",x,")=",fact_1(x)

print "-"*60
#2
print "рекурсивный метод"
for x in range(1,6):
    print "fact_2(",x,")=",fact_2(x)

   
print "-"*60

#3
print "через reduce"
for x in range(1,6):
    print "fact_3(",x,")=",fact_3(x)
