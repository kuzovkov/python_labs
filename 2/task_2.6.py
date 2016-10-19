#Кузовков Александр Владимирович

def reverse_num(num):
    stroka=str(num)
    ls=list(stroka)
    ls.reverse()
    if ls[len(ls)-1]=='-':
        ls.pop()
        ls.insert(0,'-')
    rev_stroka=''
    for c in ls:
        rev_stroka=rev_stroka+c
    return rev_stroka

def main():
    n=input('Введите количество чисел: ')
    n=int(float(n))
    ls=range(n)
    num=range(n)
    r_num=range(n)
    for i in ls:
        num[i]=raw_input('Введите число: ')
        num2=num[i]
        if num[i][0]=='-':
            num2=num[i][1:]
            
        if num2.isdigit()==False:
            print 'Вы ввели не число'
            return
        num[i]=int(num[i])

        r_num[i]=reverse_num(num[i])


    for i in ls:
        print r_num[i]


    return

    
    
main()    
