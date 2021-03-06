from Tkinter import *
import tkMessageBox

root=Tk()
root.title('pacman')
root.resizable(0,0)

# ���������� ����������
i=0
cntX=20 #���-�� ������ �� �����������
cntY=20 #���-�� ������ �� ���������
sizeCell=20 #������ ������
cell=[]
pacman=None
pacman_trend='r'
pacman_speed=5
monster_speed=3
temp_key=None
monster=[]
monster_trend=[]

c=Canvas(root,width=cntX*sizeCell,height=cntY*sizeCell,bg='#005500')
c.pack(expand=1,fill='both')

        
def tick():
    global c
    mainMove()
    check_over()
    c.after(200,tick)


def mainMove():
    global speed,pacman_trend
    pacman_move(pacman_trend,pacman_speed)
    
def setka():
    global c,cell
    cnt=0
    for i in range(cntX):
        for j in range(cntY):
            cell.append(c.create_rectangle(i*sizeCell,j*sizeCell,(i+1)*sizeCell,(j+1)*sizeCell,outline='#ffffff',tag=cnt))
            cnt+=1

def fill_clicked(e):
    global sizeCell,cntY
    row=int(e.y/sizeCell)
    col=int(e.x/sizeCell)
    num=col*cntY+row
    #print row,col
    #print num
    c.itemconfig(cell[num],fill='grey')

def pacman_create(col,row):
    global c,pacman
    pacman=c.create_oval(col*sizeCell,row*sizeCell,(col+1)*sizeCell,(row+1)*sizeCell,fill='yellow')

def check_over():
    global monster,pacman
    for i in range(len(monster)):
        if (abs(monster_coords(i)['x0']-pacman_coords()['x0']) < sizeCell/2) and (abs(monster_coords(i)['y0']-pacman_coords()['y0']) < sizeCell/2):
            exit_game()
            break

def monster_create(col,row):
    global c,monster
    monster.append(c.create_oval(col*sizeCell,row*sizeCell,(col+1)*sizeCell,(row+1)*sizeCell,fill='#550000'))
    
def pacman_coords():
    global c,pacman
    ls=c.coords(pacman)
    coord={'x0':ls[0],'y0':ls[1],'x1':ls[2],'y1':ls[3]}
    return coord

def monster_coords(k):
    global monster,c
    ls=c.coords(monster[k])
    coord={'x0':ls[0],'y0':ls[1],'x1':ls[2],'y1':ls[3]}
    return coord

def pacman_move(trend,speed):
    global c,pacman
    if trend=='r':
        if pacman_coords()['x1'] < cntX*sizeCell:
            c.move(pacman,speed,0)
    if trend=='l':
        if pacman_coords()['x0'] > 0:
            c.move(pacman,-speed,0)
    if trend=='u':
        if pacman_coords()['y0'] > 0:
            c.move(pacman,0,-speed)
    if trend=='d':
        if pacman_coords()['y1'] < cntY*sizeCell:
            c.move(pacman,0,speed)

def monster_move(i,trend,speed):
    global c,monster
    if trend=='r':
        if pacman_coords()['x1'] < cntX*sizeCell:
            c.move(pacman,speed,0)
    if trend=='l':
        if pacman_coords()['x0'] > 0:
            c.move(pacman,-speed,0)
    if trend=='u':
        if pacman_coords()['y0'] > 0:
            c.move(pacman,0,-speed)
    if trend=='d':
        if pacman_coords()['y1'] < cntY*sizeCell:
            c.move(pacman,0,speed)


    
def select_trend(e):
    global pacman_trend,speed,temp_key
    if temp_key==e.keysym:
        return
    if e.keysym=='Up':
        temp_trend='u'
    if e.keysym=='Down':
        temp_trend='d'
    if e.keysym=='Left':
        temp_trend='l'
    if e.keysym=='Right':
        temp_trend='r'
    temp_key=e.keysym
    if pacman_trend=='l' or pacman_trend=='r':
        while pacman_coords()['x1']%sizeCell !=0:
            mainMove()
        pacman_trend=temp_trend
        return
    if pacman_trend=='u' or pacman_trend=='d':
        while pacman_coords()['y1']%sizeCell !=0:
            mainMove()
        pacman_trend=temp_trend
        return

def exit_game():
    tkMessageBox.showwarning('Pacman','Game Over!')
    root.destroy()

c.after(500,tick)
setka()
pacman_create(1,2)
monster_create(16,14)
monster_create(6,8)
monster_create(1,10)


c.bind('<1>',fill_clicked)
root.bind('<KeyPress>',select_trend)

root.mainloop()
