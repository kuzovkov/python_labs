#Кузовков Александр Владимирович
def main():
    print 'введите целое число не более 3х разрядов:'
    a=raw_input()
    if a=='':
        a=0
    a=abs(int(a))
    if a > 999:
        print 'в числе более 3х разрядов'
        if quit():
            return
        else: main()
        
    s=a/100
    d=(a-s*100)/10
    e=a-s*100-d*10
    print 'В введеном числе:'
    print 'сотен: ',s
    print 'десятков: ',d
    print 'единиц:', e
    if quit():
        return
    else:
        main()

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

    

main()
