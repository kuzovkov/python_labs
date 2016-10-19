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
    print 'введите температуру в градусах Цельсия'
    c=input()
    c=float(c)
    f=9*c/5+32
    print c,'градусов по Цельсию соответсвуют',f,'градусов по Фаренгейту'
    if quit():
        return
    else:
        main()

main()
    
