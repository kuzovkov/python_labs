#�������� ��������� ������������

def main():
    spisok=range(10)
    for i in range(len(spisok)):
        spisok[i]=input('������� '+str(i+1)+' ������� ������: ')
    print '���������� ��������: ',min(spisok)
    print '���������� ��������: ',max(spisok)
    
    summa=0
    for elem in spisok:
        summa=summa+elem
    

    print '������� ��������������: ',float(summa)/len(spisok)
    print '�������� �������: ',spisok[len(spisok)-1]

    return


main()
        
