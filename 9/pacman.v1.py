from Tkinter import *
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
speed=5
temp_key=None

c=Canvas(root,width=cntX*sizeCell,height=cntY*sizeCell,bg='#005500')
c.pack(expand=1,fill='both')

        
def tick():
    global c,speed,pacman_trend
    mainMove()
    c.after(200,tick)


def mainMove():
    global c,speed,pacman_trend
    pacman_move(pacman_trend,speed)
    
def setka():
    global c,cell
    cnt=0
    for i in range(cntX):
        for j in range(cntY):
            cell.append(c.create_rectangle(i*sizeCell,j*sizeCell,(i+1)*sizeCell,(j+1)*sizeCell,outline='#ffffff',tag=cnt))
            #c.tag_bind(cell[len(cell)-1],'<1>',click)
            cnt+=1

def fill_clicked(e):
    global sizeCell,cntY
    row=int(e.y/sizeCell)
    col=int(e.x/sizeCell)
    num=col*cntY+row
    #print row,col
    #print num
    c.itemconfig(cell[num],fill='grey')

def pacman_bond(col,row):
    global c,pacman
    pacman=c.create_oval(col*sizeCell,row*sizeCell,(col+1)*sizeCell,(row+1)*sizeCell,fill='yellow')
    
def pacman_coords():
    global c,pacman
    ls=c.coords(pacman)
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
    if trend=='s':
        pass
    
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


c.after(2000,tick)
setka()
pacman_bond(1,2)


c.bind('<1>',fill_clicked)
root.bind('<KeyPress>',select_trend)

root.mainloop()
