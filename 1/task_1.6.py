#Кузовков Александр Владимирович
import math
def quit():
    print "Для выхода введите q"
    c=raw_input()
    if c=='':
        c='1'
    c=c[0]
    if c =='q':
        return True
    else:
        return False


def main():
    print 'введите координаты 1ой точки x1,y1:'
    x1,y1=input()
    print 'введите координаты 2ой точки x2,y2:'
    x2,y2=input()
    rast=math.sqrt((x1-x2)**2+(y1-y2)**2)
    print 'расстояние=',rast
    if quit():
        return
    else:
        main()

main()


