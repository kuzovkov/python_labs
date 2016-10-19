#Кузовков Александр Владимирович





def fib(n):
    if n<3:
        return 1
    else:
        
        return fib(n-1) + fib(n-2)


n=input("Введите номер числа Фибоначчи: ")

print "Число Фибоначчи с номером",n," = ",fib(n)




        
        
    
