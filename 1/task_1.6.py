#�������� ��������� ������������
import math
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
    print '������� ���������� 1�� ����� x1,y1:'
    x1,y1=input()
    print '������� ���������� 2�� ����� x2,y2:'
    x2,y2=input()
    rast=math.sqrt((x1-x2)**2+(y1-y2)**2)
    print '����������=',rast
    if quit():
        return
    else:
        main()

main()


