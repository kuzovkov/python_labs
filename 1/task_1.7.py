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
    print '������� ����������� � �������� �������'
    c=input()
    c=float(c)
    f=9*c/5+32
    print c,'�������� �� ������� ������������',f,'�������� �� ����������'
    if quit():
        return
    else:
        main()

main()
    
