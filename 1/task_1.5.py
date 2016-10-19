#Кузовков Александр Владимирович
def poud(a,x):
    rez=1
    x=int(x)
    if x==0:
        return 1
    while x:
        rez=rez*a
        x=x-1
    return rez

def quit():
    print "Для выхода введите q"
    c=raw_input()
    if c=='':
        c='1'
    c=c[0]
    if c =='q':
        return True
    else:
        return False
    
def main():
    
    print 'введите двоичное число:'

    stroka=raw_input()
    str_len=len(stroka)
    #print 'strlen=',str_len
    decimal=0
    n=str_len-1
    while n >= 0:
        #print stroka[n]

        if stroka[n] == '1':
            decimal=decimal+poud(2,(str_len-(n+1)))
        n=n-1

    print stroka,'=',decimal
    if quit():
        return
    else:
        main()

main()




        
        
