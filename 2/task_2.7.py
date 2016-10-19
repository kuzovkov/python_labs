#Кузовков Александр Владимирович

def str_shift(str_in,n):
    return str_in[n:]+str_in[:n]

def main():
    stroka=raw_input('Введите строку: ')
    n=len(stroka)
    i=0
    while i<=n-1:
        print stroka
        stroka=str_shift(stroka,2)
        i=i+2
       


    return

main()
    
    
