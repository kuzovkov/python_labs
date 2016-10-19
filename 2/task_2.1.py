#�������� ��������� ������������

import math

#���������� ����� �������
def dlina(dot1,dot2):
    return math.sqrt((dot1[0]-dot2[0])**2+(dot1[1]-dot2[1])**2)

#����������� ����� �� ��� ����� �� ������
def online(dot1,dot2,dot3):
    if dlina(dot1,dot2)+dlina(dot2,dot3)==dlina(dot1,dot3):
        return True
    elif dlina(dot1,dot3)+dlina(dot2,dot3)==dlina(dot1,dot2):
        return True
    elif dlina(dot1,dot2)+dlina(dot1,dot3)==dlina(dot2,dot3):
        return True
    else:
        return False
    

def main():
    x1,y1=input('������� ���������� 1�� ����� x,y:')
    x2,y2=input('������� ���������� 2�� ����� x,y:')
    x3,y3=input('������� ���������� 3�� ����� x,y:')
    x4,y4=input('������� ���������� 4�� ����� x,y:')


    dot1=(x1,y1)
    dot2=(x2,y2)
    dot3=(x3,y3)
    dot4=(x4,y4)

    f_dlina=1

    if dlina(dot1,dot2)==dlina(dot3,dot4):
        f_dlina=f_dlina+1
    if dlina(dot1,dot3)==dlina(dot2,dot4):
        f_dlina=f_dlina+1
    if dlina(dot1,dot4)==dlina(dot2,dot3):
        f_dlina=f_dlina+1

    f_online=0

    if online(dot1,dot2,dot3):
        f_online=1
    if online(dot1,dot2,dot4):
        f_online=1
    if online(dot2,dot3,dot4):
        f_online=1
    if online(dot1,dot3,dot4):
        f_online=1

    if f_dlina >=2 and f_online==0:
        print "����� ��������������"
        return
    else:
        print "����� �� ��������������"
        return
main()

    

    

    
                
                
    
