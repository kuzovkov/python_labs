#�������� ��������� ������������
def main():
    print '������� ����� ����� �� ����� 3� ��������:'
    a=raw_input()
    if a=='':
        a=0
    a=abs(int(a))
    if a > 999:
        print '� ����� ����� 3� ��������'
        if quit():
            return
        else: main()
        
    s=a/100
    d=(a-s*100)/10
    e=a-s*100-d*10
    print '� �������� �����:'
    print '�����: ',s
    print '��������: ',d
    print '������:', e
    if quit():
        return
    else:
        main()

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

    

main()
