#�������� ��������� ������������
def quit():
    print "��� ������ ������� q"
    c=raw_input()
    if c=='':
        c='1'
    c=c[0]
    if c =='q':
        return True
    else:
        return False

def main():
    num=raw_input('������� �����: ')
    if num=='':
        num=0
    num=int(float(num))

    q=0
    
    for i in range(1,num+1):
        q=q+(2*i-1)

    
    print '������� ����� ',num,' ����� ',q
    if quit():
        return
    else:
        main()
    

main()
    
