#coding=utf-8
#метод Ньтона
import fpformat
from Tkinter import *
import func
from math import sqrt

root = Tk()
root.geometry('1024x500')
root.title('Метод Ньютона')

#globals variables
F1=0 #Значения функции в точках x1, x2
F2=0
x1=0
x2=0
t=0 #коэф. золотого сечения
eps = func.eps #заданная точность
a = func.a #границы интервала текущие
b = func.b
count=0 #счетчик итераций
a0 = a #границы интервала заданные
b0 = b
epsCurrent =  b0-a0 #текущая точность
canvasWidth = 400 #размеры canvas
canvasHeight = 400
function = '' #описание функции
lines=[]
intervals=[]
colors=['#334455','#2ddd67','#85ccc1','#267373','#284848']
entryA = StringVar()
entryB = StringVar()
entryA.set(str(a0))
entryB.set(str(b0))

def getFunction():
    global function, a0,b0
    function='функция: '+ func.formula
    function += 'interval: '+fpformat.fix((float(a0)),2) + ' - ' + fpformat.fix(str(float(b0)),2)
    function += '   eps= ' + str( eps )
    return function

#function
def F( x ):
    return func.function( x )

    
def paintFunc(color='red',width=2):
    count = 200
    delta = abs(float((b0-a0))/count)
    x=a0
    ymax = F( x )
    ymin = F( x )
    while x < b0:
        if ymax < F(x): ymax = F(x)
        if ymin > F(x): ymin = F(x)
        x += delta    
    labelYmax.configure( text = fpformat.fix(ymax, 1) )
    labelYmin.configure( text = fpformat.fix(ymin, 1) )
    kx = canvasWidth/abs(float(b0-a0)) 
    ky = canvasHeight/abs(float(ymax-ymin))
    x=a0
    c.create_line(10,canvasHeight,canvasWidth,canvasHeight,width=2, arrow=LAST)
    c.create_line(10,canvasHeight,10,0,width=2,arrow=LAST)
    #print '-'*60
    while x < b0:
        #print kx*(x-a0)+10, canvasHeight - ky*(F(x)-ymin), kx*((x-a0)+delta)+10,canvasHeight-ky*(F(x+delta)-ymin)
        c.create_line(kx*(x-a0)+10, canvasHeight - ky*(F(x)-ymin), kx*((x-a0)+delta)+10,canvasHeight-ky*(F(x+delta)-ymin),width=width,fill=color)
        x += delta
        
def paintVertLine(x,color):
    global lines
    kx =canvasWidth /float(b0-a0)
    lines.append( c.create_line(kx*(x-a0)+10, 0, kx*(x-a0)+10,canvasHeight,width=1,fill=color) )

def paintInterval(x1,x2,color='blue',width=5):
    global intervals
    kx = 400/float(b0-a0)
    intervals.append( c.create_line(kx*(x1-a0)+10, canvasHeight, kx*(x2-a0)+10,canvasHeight,width=width,fill=color) )



def start_gold():
    global t,x1,x2,F1,F2,a,b
    
    t = ( sqrt( 5 ) -1 ) / 2
    x1 = b0 - t * ( b0 - a0 )
    x2 = a0 + t * ( b0 - a0 )
    F1 = F( x1 )
    F2 = F( x2 )
    
def nextIt():
    global eps,a,b,colors,count,lines,textbox,epsCurrent,F1,F2,t,x1,x2

    if F1 < F2:
        b = x2
        x2=x1
        F2=F1
        x1 = b - t * ( b - a )
        F1 = F( x1 )
    else:
        a = x1
        x1=x2
        F1=F2
        x2=a + t * ( b - a )
        F2=F(x2)

    string=str(count)+' a= '+str(a)+' b= '+str(b)+' x1 = '+str(x1)+' x2= '+str(x2)+' F((a+b)/2)= '+str( F( (a+b) / 2 ))+'\n'
    textbox.insert(END,string)
    count += 1
       
    if len(lines) != 0:
        c.delete(lines[len(lines)-1])
    paintVertLine( (a+b)/2,colors[count%5])
    if len(intervals) != 0:
        c.delete(intervals[len(intervals)-1])
    paintInterval(a,b)
    epsCurrent = b - a
    writeEps()

def writeEps():
    global epsCurrent, eps, labelEps
    if epsCurrent <= eps:
        fg = 'green'
    else:
        fg = 'red'
    labelEps.configure( text='интервал неопр.:' + fpformat.fix(float(epsCurrent),6), fg = fg)
    

def reset():
    global intervals, lines, a, b, a0, b0, c, tetxbox,count,epsCurrent
    a0 = float(entryA.get())
    b0 = float(entryB.get())
    a=a0
    b=b0
    c.delete(ALL)
    textbox.delete(1.0,END)
    paintFunc()
    count = 0
    epsCurrent = b - a
    writeEps()
    labelFunc.configure( text = getFunction() )
    start_gold()
        

#canvas
c=Canvas(root,width=canvasWidth,height=canvasHeight,bg='#ffffff',bd=3)
c.place( x=30, y =30 )

#labels
labelFunc=Label(root, text = getFunction(), font='Arial 14', fg='blue')
labelFunc.place(x=30, y=0)
labelA = Entry(root, textvariable = entryA, font='Arial 14',width = 3)
labelA.place(x=30,y=440)
labelB=Entry(root, textvariable = entryB, font='Arial 14',width =3)
labelB.place(x=400,y=440)
labelYmax = Label(root,text = '0', font='Arial 14')
labelYmax.place(x = 0, y = 20)
labelYmin = Label(root,text = '0', font='Arial 14')
labelYmin.place(x = 0, y = 400)
labelEps = Label(root,text = '', font = 'Arial 14')
labelEps.place(x=700,y=0)

#buttons
btn_next=Button(root,text='Next', font='Arial 14', command=lambda: nextIt() )
btn_next.place(x=130,y=450)
btn_reset=Button(root,text='Reset', font='arial 14', command=lambda: reset() )
btn_reset.place(x=280, y=450)

#textbox
textbox = Text(root,font='Arial 8', width = 80, height = 32)
textbox.place(x=480, y= 30)

#scroll
scroll=Scrollbar(root)
scroll.pack(side='right', fill='y')

textbox['yscrollcommand'] = scroll.set
scroll['command'] = textbox.yview



paintFunc()
writeEps()
start_gold()

root.mainloop()




