#Кузовков Александр Владимирович

def is_simple(n):  #проверка простое ли число
    for x in range(2,n):
        if n%x ==0:
            return False
    return True

def simple(n):
    n=int(n)
    ls=range(1,n+1)
    return filter(lambda x:is_simple(x),ls)


n=input('Введите простое число:')



print "Простые числа до ",n,": ",simple(n)


    
    
