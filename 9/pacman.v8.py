from Tkinter import *
import tkMessageBox
from random import * 

root=Tk()
root.title('pacman')
root.resizable(0,0)

# глобальные переменные
i=0

score=0# набранные очки
timer=None #главный таймер
btn_save=None # идентификаторы кнопок
btn_start=None
btn_pause=None
btn_exit=None
btn_config=None
label_score=None
cntX=20 #кол-во клеток по горизонтали
cntY=20 #кол-во клеток по вертикали
sizeCell=20 #размер клетки
cell=[]#список клеток
pacman=None #пакман
pacman_img=PhotoImage(file='pacman.gif')
monster_img=PhotoImage(file='monster.gif')
bonus_img=PhotoImage(file='bonus.gif')
pacman_trend='r' #направление движени€ пакмана
pacman_speed=5 #скорость пакмана
monster_speed=4 #скорость монстров
temp_key=None
monster=[] # список монстров
monster_trend=[] # список направлений движени€ дл€ монстров 
monster_fpov=[] #список флагов поворота дл€ монстров
pacman_fpov=0 #флаг поворота дл€ пакмана
wall=[90,91,92,93,94,95,96,97,98,110,130,150,170,190,210,230,250] #стена
bonus=[155,165,175,185,195,205,215,225]#бонусы
ls_bonus={} #словарь изображений бонусов
c=Canvas(root,width=cntX*sizeCell,height=cntY*sizeCell,bg='#005500')
c.pack(expand=1,fill='both')

        
def tick(): #главный цикл
    global c,timer
    mainMove()
    check_cross_monster()
    check_cross_bonus()
    timer=c.after(200,tick)


def mainMove():  #квант движени€ персонажей
    global pacman_speed,pacman_trend
    pacman_move(pacman_trend,pacman_speed)
    for i in range(len(monster)):
        monster_move(i,monster_trend[i],monster_speed)
    
def setka(): #отрисовка сетки пр€моугольниками
    global c,cell
    cnt=0
    for i in range(cntX):
        for j in range(cntY):
            cell.append(c.create_rectangle(i*sizeCell,j*sizeCell,(i+1)*sizeCell,(j+1)*sizeCell,outline='#ffffff'))
            cnt+=1

def wall_create(): #отрисовка стены
    global sizeCell,cntY,wall,cell,c
    for i in range(len(cell)):
        if i in wall:
            c.itemconfig(cell[i],fill='grey')


def bonus_create():  #отрисовка бонусов
    global bonus,cell,c,ls_bonus
    for i in range(len(cell)):
        if i in bonus:
            ls_bonus.update({i:c.create_image(cell_coords(i)['x0'],cell_coords(i)['y0'],image=bonus_img,anchor='nw')})
        

def pacman_create(col,row): # создание пакмана
    global c,pacman,cntY,wall
    num=row+col*cntY
    while num in wall:
        row+=1
        num=row+col*cntY
    pacman=c.create_image(col*sizeCell,row*sizeCell,image=pacman_img,anchor='nw')

def check_cross_monster():  #проверка пересечени€ пакмана с монстром
    global monster,pacman
    for i in range(len(monster)):
        if (abs(monster_coords(i)['x0']-pacman_coords()['x0']) < sizeCell/2) and (abs(monster_coords(i)['y0']-pacman_coords()['y0']) < sizeCell/2):
            game_over()
            break

def check_cross_bonus(): #проверка пересечени€ пакмана с бонусом
    global pacman,bonus,cell,score,label_score,c
    for i in bonus:
        if (abs(pacman_coords()['x0']-cell_coords(i)['x0'])==0) and (abs(pacman_coords()['y0']-cell_coords(i)['y0'])==0):
            c.delete(ls_bonus[i])
            del ls_bonus[i]
            del bonus[bonus.index(i)]
            
            score+=10
            label_score.config(text='Score:' +str(score))
            if len(bonus)==0:
                congratulations()
                break
            
def monster_see_pacman(i): #i-й монстр увидел пакмана
    global monster,pacman,sizeCell,monster_fpov
    px0=pacman_coords()['x0']
    py0=pacman_coords()['y0']
    px1=pacman_coords()['x1']
    py1=pacman_coords()['y1']

    mx0=monster_coords(i)['x0']
    my0=monster_coords(i)['y0']
    mx1=monster_coords(i)['x1']
    my1=monster_coords(i)['y1']

    if (abs(my0-py0)<sizeCell/2) and (abs(px0-mx0)<sizeCell*8) and (px0>mx0):
        return 'r'
    else:
        if (abs(my0-py0)<sizeCell/2) and (abs(px0-mx0)<sizeCell*8) and (px0<mx0):
            return 'l'
        else:
            if (abs(mx0-px0)<sizeCell/2) and (abs(my0-py0)<sizeCell*8) and (my0<py0):
                return 'd'
            else:
                if (abs(mx0-px0)<sizeCell/2) and (abs(my0-py0)<sizeCell*8) and (my0>py0):
                    return 'u'
                else:
                    return False


def monster_create(col,row,trend): # создание монстра
    global c,monster,monster_trend,monster_fpov,wall
    num=row+col*cntY
    while num in wall:
        row+=1
        num=row+col*cntY
    monster.append(c.create_image(col*sizeCell,row*sizeCell,image=monster_img,anchor='nw'))
    monster_trend.append(trend)
    monster_fpov.append(0)
    
def pacman_coords(): #получение координат пакмана
    global c,pacman,sizeCell
    ls=c.coords(pacman)
    coord={'x0':ls[0],'y0':ls[1],'x1':ls[0]+sizeCell,'y1':ls[1]+sizeCell}
    return coord

def monster_coords(k):#получение координат k-го монстра
    global monster,c,sizeCell
    ls=c.coords(monster[k])
    coord={'x0':ls[0],'y0':ls[1],'x1':ls[0]+sizeCell,'y1':ls[1]+sizeCell}
    return coord

def cell_coords(i): #получение кординат i-й €чейки 
    global c,cell
    ls=c.coords(cell[i])
    coord={'x0':ls[0],'y0':ls[1],'x1':ls[2],'y1':ls[3]}
    return coord

def check_wall_pacman(trend): #проверка встречи пакмана со стеной
    global sizeCell,wall
    result=False
    px0=pacman_coords()['x0']
    py0=pacman_coords()['y0']
    for num_cell in wall:
        cx0=cell_coords(num_cell)['x0']
        cy0=cell_coords(num_cell)['y0']
        
        if trend=='r':
            if (cx0-px0<=sizeCell) and (cy0==py0) and (cx0>px0):
                return True
            else:
                result=False
        else:
            if trend=='l':
                if (px0-cx0<=sizeCell) and (cy0==py0) and (cx0<px0):
                    return True
                else:
                    result=False
                
            else:
                if trend=='u':
                    if (py0-cy0<=sizeCell) and (cx0==px0) and (cy0<py0):
                        return True
                    else:
                        result=False
                else:
                    if trend=='d':
                        if (cy0-py0<=sizeCell) and (cx0==px0) and (cy0>py0):
                            return True
                        else:
                            result=False
                    else:
                        result=False
    return result


def check_wall_monster(i,trend): #проверка встречи i-го монстра со стеной
    global sizeCell,wall
    result=False
    px0=monster_coords(i)['x0']
    py0=monster_coords(i)['y0']
    for num_cell in wall:
        cx0=cell_coords(num_cell)['x0']
        cy0=cell_coords(num_cell)['y0']
        
        if trend=='r':
            if (cx0-px0<=sizeCell) and (cy0==py0) and (cx0>px0):
                return True
            else:
                result=False
        else:
            if trend=='l':
                if (px0-cx0<=sizeCell) and (cy0==py0) and (cx0<px0):
                    return True
                else:
                    result=False
                
            else:
                if trend=='u':
                    if (py0-cy0<=sizeCell) and (cx0==px0) and (cy0<py0):
                        return True
                    else:
                        result=False
                else:
                    if trend=='d':
                        if (cy0-py0<=sizeCell) and (cx0==px0) and (cy0>py0):
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
        if (monster_coords(i)['x1'] < cntX*sizeCell) and (not check_wall_monster(i,'r')):
            c.move(monster[i],speed,0)
        else:
            monster_trend[i]='l'
    if trend=='l':
        if (monster_coords(i)['x0'] > 0) and (not check_wall_monster(i,'l')):
            c.move(monster[i],-speed,0)
        else:
            monster_trend[i]='r'
    if trend=='u':
        if (monster_coords(i)['y0'] > 0) and (not check_wall_monster(i,'u')):
            c.move(monster[i],0,-speed)
        else:
            monster_trend[i]='d'
    if trend=='d':
        if (monster_coords(i)['y1'] < cntY*sizeCell) and (not check_wall_monster(i,'d')):
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
    if monster_see_pacman(i) != False:
        monster_fpov[i]=monster_see_pacman(i)
    
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


def gen_monster_trend():#генераци€ случайного направлени€ движени€ монстра
    x=randrange(0,400,1)
    if x<100:
        return 'l'
    if 99 < x < 200:
        return 'u'
    if 199 < x < 300:
        return 'r'
    else: return 'd'
    
def change_monster_trend():#изменение направлени€ движени€ монстров 
    global monster_fpov
    for i in range(len(monster_fpov)):
        monster_fpov[i]=gen_monster_trend()   
    root.after(5000,change_monster_trend)    
    

def game_over():# game over
    tkMessageBox.showwarning('Pacman','Game Over!')
    root.destroy()

def exit_game():
    if tkMessageBox.askokcancel('Pacman','Exit Game?'):
        root.destroy()

def congratulations():
    global score
    tkMessageBox.showinfo('Pacman','Congratulations!!!\nYou score: '+str(score))
    root.destroy()

def start_game():
    c.after(500,tick)#запуск цикла движени€


def pause_game():
    global timer,c
    if timer != None:
        c.after_cancel(timer)




def wall_config(e): #редактирование стен
    global wall,sizeCell,cell,c
    col=int(e.x/sizeCell)
    row=int(e.y/sizeCell)
    num=row+col*cntY
    if num in wall:
        del wall[wall.index(num)]
        c.itemconfig(cell[num],fill='#005500')
    else:
        if num not in bonus:
            wall.append(num)
            c.itemconfig(cell[num],fill='grey')


def bonus_config(e): #редактирование бонусов
    global wall,bonus,ls_bonus,cell,c,sizeCell
    col=int(e.x/sizeCell)
    row=int(e.y/sizeCell)
    num=row+col*cntY
    if num in wall:
        del wall[wall.index(num)]
        c.itemconfig(cell[num],fill='#005500')
        bonus.append(num)
    if num in bonus:
        del bonus[bonus.index(num)]
        if ls_bonus.has_key(num):
            c.delete(ls_bonus[num])
            del ls_bonus[num]
    else:
        bonus.append(num)
        ls_bonus.update({num:c.create_image(cell_coords(num)['x0'],cell_coords(num)['y0'],image=bonus_img,anchor='nw')})


def save_config(): #переход от конфигурации к игре
    global btn_save,btn_exit,ls_bonus,c
    btn_exit.destroy()
    btn_save.destroy()
    for i in ls_bonus.keys():
        c.delete(ls_bonus[i])
    ls_bonus.clear()
    c.bind('<1>',stub)
    c.bind('<3>',stub)
    init_game()
    
def stub(e):
    pass


def config_pole(): #редактированик пол€
    global monster,monster_fpov,monster_trend,c,btn_save,ls_bonus,c,hand1,hand2
    pause_game()
    c.delete(pacman)
    pacman_fpov=0
    for i in range(len(monster)):
        c.delete(monster[i])
    monster=[]
    monster_trend=[]
    monster_fpov=[]
    btn_start.destroy()
    btn_config.destroy()
    btn_pause.destroy()
    label_score.destroy()
    
   
    btn_save=Button(root,text='save',font='Arial 12',width=6,command=save_config)
    btn_save.pack(side='left')

    c.bind('<1>',wall_config)
    c.bind('<3>',bonus_config)


def button():#кнопки
    global btn_config,btn_start,btn_pause,btn_exit,label_score
    btn_config=Button(root,text='config',width=6,font='Arial 12',command=config_pole)
    btn_config.pack(side='left')
    btn_start=Button(root,text='start',width=6,font='Arial 12',command=start_game)
    btn_start.pack(side='left')
    btn_pause=Button(root,text='pause',width=6,font='Arial 12',command=pause_game)
    btn_pause.pack(side='left')
    btn_exit=Button(root,text='exit',width=6,font='Arial 12',command=exit_game)
    btn_exit.pack(side='left')
    label_score=Label(root,text='Score: '+str(score),font='Arial 12',bg='#ffffff',fg='#ff0000')
    label_score.pack(side='right')   


def init_game():
    global score
    setka()# отрисовка сетки
    wall_create() #создание стен
    bonus_create() #отрисовка бонусов
    pacman_create(1,2) #создание ѕакмана и монстров
    monster_create(16,14,'l')
    monster_create(6,8,'r')
    monster_create(1,10,'u')
    score=0
    button()
    
        


init_game()
change_monster_trend()# запуск функции случайного изменени€ направлени€ движени€ монстров



#прив€зка нажатий клавиш и мыши

root.bind('<KeyPress>',select_trend)



root.mainloop()
