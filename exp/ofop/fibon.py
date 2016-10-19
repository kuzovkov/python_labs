#coding=utf-8
#метод Фибоначчи f(x)=0.7*x2-sqrt(3)*x +4.8
import fpformat
from Tkinter import *
import func

root = Tk()
root.geometry('1024x500')
root.title('Метод Фибоначчи')

#globals variables
eps = func.eps #заданная точность
a = func.a #границы интервала текущие
b = func.b
count=0 #счетчик итераций
a0 = a #границы интервала заданные
b0 = b
N = 30 #номер числа Фибоначчи
F1 = 0
F2 = 0
x1 = 0
x2 = 0
epsCurrent =  b0-a0 #текущая точность
canvasWidth = 400
canvasHeight = 400
function = '' #описание функции
lines=[]
intervals=[]
colors=['#334455','#2ddd67','#85ccc1','#267373','#284848']
entryA = StringVar()
entryB = StringVar()
entryN = StringVar()
entryA.set(str(a0))
entryB.set(str(b0))
entryN.set(str(N))


def fib( n ):
    if n < 3:
        return 1
    else:
        return ( fib( n-1 ) + fib( n-2 ) )
    
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

def start_fib():
    global a0,b0,N,x1,x2
    x1 = b0 - ( float( fib( N ) )/ fib( N + 1 ) )  * ( b0 - a0 )
    if x1 > (a0 + b0)/2:
        x1=a0+b0-x1
    x2=a0+b0-x1

def nextIt():
    global eps,a,b,colors,count,lines,textbox,epsCurrent,x1,x2,F1,F2
    F1 = F(x1)
    F2 = F(x2)
    if F1 > F2:
        a = x1
        x1 = x2
    else:
        b = x2
    if x1 > (a + b)/float(2):
        x1=a+b-x1
    x2=a+b-x1
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
    global intervals, lines, a, b, a0, b0, N,c, tetxbox,count,epsCurrent
    a0 = float(entryA.get())
    b0 = float(entryB.get())
    N = float(entryN.get())
    a=a0
    b=b0
    c.delete(ALL)
    textbox.delete(1.0,END)
    paintFunc()
    count = 0
    epsCurrent = b - a
    writeEps()
    labelFunc.configure( text = getFunction() )
    start_fib()
        
#canvas
c=Canvas(root,width=canvasWidth,height=canvasHeight,bg='#ffffff',bd=3)
c.place( x=30, y =30 )

#labels
labelFunc=Label(root, text = getFunction(), font='Arial 14', fg='blue')
labelFunc.place(x=30, y=0)
labelN=Entry(root,textvariable = entryN, font='Arial 14', width = 3)
labelN.place(x=170, y= 450)
labelF=Label(root, text = 'Np=', font='Arial 14', width = 3)
labelF.place(x=120, y= 450)
labelA=Entry(root, textvariable = entryA, font='Arial 14',width = 3)
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
btn_next.place(x=230,y=450)
btn_reset=Button(root,text='Reset', font='arial 14', command=lambda: reset() )
btn_reset.place(x=320, y=450)

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
start_fib()

root.mainloop()




