from Tkinter import *
import tkMessageBox
from random import * 

root=Tk()
root.title('pacman')
root.resizable(0,0)

# глобальные переменные
i=0
cntX=20 #кол-во клеток по горизонтали
cntY=20 #кол-во клеток по вертикали
sizeCell=20 #размер клетки
cell=[]
pacman=None
pacman_trend='r'
pacman_speed=5
monster_speed=3
temp_key=None
monster=[] # список монстров
monster_trend=[] # список напрвлений движения для монстров 
monster_fpov=[] #список флагов поворота для монстров
pacman_fpov=0 #флаг поворота для пакмана
wall=[90,91,92,93] #стена

c=Canvas(root,width=cntX*sizeCell,height=cntY*sizeCell,bg='#005500')
c.pack(expand=1,fill='both')

        
def tick(): #главный цикл
    global c
    mainMove()
    check_over()
    c.after(200,tick)


def mainMove():  #квант движения персонажей
    global pacman_speed,pacman_trend
    pacman_move(pacman_trend,pacman_speed)
    for i in range(len(monster)):
        monster_move(i,monster_trend[i],monster_speed)
    
def setka(): #отрисовка сетки прямоугольниками
    global c,cell
    cnt=0
    for i in range(cntX):
        for j in range(cntY):
            cell.append(c.create_rectangle(i*sizeCell,j*sizeCell,(i+1)*sizeCell,(j+1)*sizeCell,outline='#ffffff'))
            cnt+=1

def wall_create():
    global sizeCell,cntY,wall,cell,c
    for i in range(len(cell)):
        if i in wall:
            c.itemconfig(cell[i],fill='grey',tag='wall')


    

def pacman_create(col,row): # создание пакмана
    global c,pacman
    pacman=c.create_oval(col*sizeCell,row*sizeCell,(col+1)*sizeCell,(row+1)*sizeCell,fill='yellow')

def check_over():  #проверка пересечения пакмана с монстром
    global monster,pacman
    for i in range(len(monster)):
        if (abs(monster_coords(i)['x0']-pacman_coords()['x0']) < sizeCell/2) and (abs(monster_coords(i)['y0']-pacman_coords()['y0']) < sizeCell/2):
            game_over()
            break

def monster_create(col,row,trend): # создание монстра
    global c,monster,monster_trend,monster_fpov
    monster.append(c.create_oval(col*sizeCell,row*sizeCell,(col+1)*sizeCell,(row+1)*sizeCell,fill='#550000'))
    monster_trend.append(trend)
    monster_fpov.append(0)
    
def pacman_coords(): #получение координат пакмана
    global c,pacman
    ls=c.coords(pacman)
    coord={'x0':ls[0],'y0':ls[1],'x1':ls[2],'y1':ls[3]}
    return coord

def monster_coords(k):#получение координат k-го монстра
    global monster,c
    ls=c.coords(monster[k])
    coord={'x0':ls[0],'y0':ls[1],'x1':ls[2],'y1':ls[3]}
    return coord

def cell_coords(i): #получение кординат i-й ячейки 
    global c,cell
    ls=c.coords(cell[i])
    coord={'x0':ls[0],'y0':ls[1],'x1':ls[2],'y1':ls[3]}
    return coord

def check_wall_pacman(trend): #проверка встречи пакмана со стеной
    global sizeCell,wall
    result=False
    for num_cell in wall:
        
        if trend=='r':
            if (cell_coords(num_cell)['x0']-pacman_coords()['x0']<=sizeCell) and (cell_coords(num_cell)['y0']==pacman_coords()['y0']) and (cell_coords(num_cell)['x0']>pacman_coords()['x0']):
                return True
            else:
                result=False
        else:
            if trend=='l':
                if (pacman_coords()['x0']-cell_coords(num_cell)['x0']<=sizeCell) and (cell_coords(num_cell)['y0']==pacman_coords()['y0']) and (cell_coords(num_cell)['x0']<pacman_coords()['x0']):
                    return True
                else:
                    result=False
                
            else:
                if trend=='u':
                    if (pacman_coords()['y0']-cell_coords(num_cell)['y0']<=sizeCell) and (cell_coords(num_cell)['x0']==pacman_coords()['x0']) and (cell_coords(num_cell)['y0']<pacman_coords()['y0']):
                        return True
                    else:
                        result=False
                else:
                    if trend=='d':
                        if (cell_coords(num_cell)['y0']-pacman_coords()['y0']<=sizeCell) and (cell_coords(num_cell)['x0']==pacman_coords()['x0']) and (cell_coords(num_cell)['y0']>pacman_coords()['y0']):
                            return True
                        else:
                            result=False
                    else:
                        result=False
    return result
                

def pacman_move(trend,speed):#движение пакмана
    global c,pacman
    if trend=='r':
        if (pacman_coords()['x1'] < cntX*sizeCell) and (not check_wall_pacman('r')):
            c.move(pacman,speed,0)
    if trend=='l':
        if (pacman_coords()['x0'] > 0) and (not check_wall_pacman('l')):
            c.move(pacman,-speed,0)
    if trend=='u':
        if (pacman_coords()['y0'] > 0) and (not check_wall_pacman('u')):
            c.move(pacman,0,-speed)
    if trend=='d':
        if (pacman_coords()['y1'] < cntY*sizeCell) and (not check_wall_pacman('d')):
            c.move(pacman,0,speed)

def monster_move(i,trend,speed): # движение i-го монстра
    global c,monster,monster_trend
    if trend=='r':
        if monster_coords(i)['x1'] < cntX*sizeCell:
            c.move(monster[i],speed,0)
        else:
            monster_trend[i]='l'
    if trend=='l':
        if monster_coords(i)['x0'] > 0:
            c.move(monster[i],-speed,0)
        else:
            monster_trend[i]='r'
    if trend=='u':
        if monster_coords(i)['y0'] > 0:
            c.move(monster[i],0,-speed)
        else:
            monster_trend[i]='d'
    if trend=='d':
        if monster_coords(i)['y1'] < cntY*sizeCell:
            c.move(monster[i],0,speed)
        else:
            monster_trend[i]='u'
    if monster_trend[i]=='l' or monster_trend[i]=='r':
        if monster_coords(i)['x1']%sizeCell == 0:
            if monster_fpov[i] !=0:
                monster_trend[i]=monster_fpov[i]
                monster_fpov[i]=0
    if monster_trend[i]=='u' or monster_trend[i]=='d':
        if monster_coords(i)['y1']%sizeCell == 0:
            if monster_fpov[i] !=0:
                monster_trend[i]=monster_fpov[i]
                monster_fpov[i]=0

    
def select_trend(e): #управление движением пакмана
    global pacman_trend,temp_key,pacman_fpov
    if temp_key==e.keysym:
        return
    if e.keysym=='Up':
        pacman_fpov='u'
    else:
        if e.keysym=='Down':
            pacman_fpov='d'
        else:
            if e.keysym=='Left':
                pacman_fpov='l'
            else:
                if e.keysym=='Right':
                    pacman_fpov='r'
                else:
                    return
    temp_key=e.keysym
    if pacman_trend=='l' or pacman_trend=='r':
        while pacman_coords()['x1']%sizeCell !=0:
            pacman_move(pacman_trend,pacman_speed)
        pacman_trend=pacman_fpov
        return
    if pacman_trend=='u' or pacman_trend=='d':
        while pacman_coords()['y1']%sizeCell !=0:
            pacman_move(pacman_trend,pacman_speed)
        pacman_trend=pacman_fpov
        return


def gen_monster_trend():#генерация случайного направления движения монстра
    x=randrange(0,400,1)
    if x<100:
        return 'l'
    if 99 < x < 200:
        return 'u'
    if 199 < x < 300:
        return 'r'
    else: return 'd'
    
def change_monster_trend():#изменение направления движения монстров 
    global monster_fpov
    for i in range(len(monster_fpov)):
        monster_fpov[i]=gen_monster_trend()   
    root.after(5000,change_monster_trend)    
    

def game_over():# game over
    tkMessageBox.showwarning('Pacman','Game Over!')
    root.destroy()

c.after(500,tick)#запуск цикла движения
setka()# отрисовка сетки
wall_create() #создание стен
pacman_create(1,2) #создание Пакмана и монстров
#monster_create(16,14,'l')
#monster_create(6,8,'r')
#monster_create(1,10,'u')
change_monster_trend()# запуск функции случайного изменения направления движения монстров



#привязка нажатий клавиш и мыши
#c.bind('<1>',fill_clicked)
root.bind('<KeyPress>',select_trend)


for i in range(len(cell)):
    if i in wall:
        print c.coords(cell[i])

root.mainloop()
