#�������� ��������� ������������

def main():
    stroka=raw_input('������� ������: ')
    ls1=list(stroka)
    ls2=ls1[:]
    ls2.reverse()
    if ls1==ls2:
        print '������ "',stroka,'" �������� �����������'
        return
    else:
        print '������ "',stroka,'" �� �������� �����������'
        return

main()
