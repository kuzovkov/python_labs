#Кузовков Александр Владимирович

def main():
    spisok=range(10)
    for i in range(len(spisok)):
        spisok[i]=input('введите '+str(i+1)+' элемент списка: ')
    print 'наименьшее значение: ',min(spisok)
    print 'наибольшее значение: ',max(spisok)
    
    summa=0
    for elem in spisok:
        summa=summa+elem
    

    print 'среднее арифметическое: ',float(summa)/len(spisok)
    print 'конечный элемент: ',spisok[len(spisok)-1]

    return


main()
        
