#Кузовков Александр Владимирович

import math

#вычисление длины отрезка
def dlina(dot1,dot2):
    return math.sqrt((dot1[0]-dot2[0])**2+(dot1[1]-dot2[1])**2)

#определение лежат ли три точки на прямой
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
    x1,y1=input('Введите координаты 1ой точки x,y:')
    x2,y2=input('Введите координаты 2ой точки x,y:')
    x3,y3=input('Введите координаты 3ой точки x,y:')
    x4,y4=input('Введите координаты 4ой точки x,y:')


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
        print "Задан параллелограмм"
        return
    else:
        print "Задан не параллелограмм"
        return
main()

    

    

    
                
                
    
