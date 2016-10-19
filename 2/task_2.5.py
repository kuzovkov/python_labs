#Кузовков Александр Владимирович
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
    num=raw_input('Введите число: ')
    if num=='':
        num=0
    num=int(float(num))

    q=0
    
    for i in range(1,num+1):
        q=q+(2*i-1)

    
    print 'квадрат числа ',num,' равен ',q
    if quit():
        return
    else:
        main()
    

main()
    
