#Кузовков Александр Владимирович

def main():
    stroka=raw_input('Введите строку: ')
    ls1=list(stroka)
    ls2=ls1[:]
    ls2.reverse()
    if ls1==ls2:
        print 'Строка "',stroka,'" является палиндромом'
        return
    else:
        print 'Строка "',stroka,'" Не является палиндромом'
        return

main()
