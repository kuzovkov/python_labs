#�������� ��������� ������������
import random

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
    print '���� "������ �����"'
    print '������� ����...'
    print '��� ���������� ������ �� ���� ������� 0'
    num_rand=random.randrange(1,25,1)
    num_user=30
    count=0
    while num_user !=0:

        num_user=raw_input('������� �����:')
        if num_user=='':
            num_user=0
        num_user=int(num_user)
        count=count+1
        if num_user > num_rand:
            print '���� ����� ������'
        elif num_user < num_rand:
            print '���� ����� ������'
        else:
            print '�� ������� �����',num_rand,'�',count,'�������'
            if quit():
                return
            else:
                main()
    
    

main()

    
