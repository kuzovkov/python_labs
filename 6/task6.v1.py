#coding=utf-8
#Кузовков Александр Владимирович
from Tkinter import *
from tkFont import *

s=''
x=0
y=0
z=0
digit=10
op='0'
new=False

app=Tk()
app.title("Калькулятор")
app.geometry('300x300')
app.resizable(0,0)


#текстовое поле
pole=Entry(app,bg="white",state="readonly",readonlybackground="white",font='Arial 20',width=18)
pole.place(x=10,y=10)


#Кнопки
btn1=Button(app,text="1",font='Arial 20')
btn1.place(x=10,y=60,width=40,height=40)


btn2=Button(app,text="2",font='Arial 20')
btn2.place(x=60,y=60,width=40,height=40)

btn3=Button(app,text="3",font='Arial 20')
btn3.place(x=110,y=60,width=40,height=40)

btn4=Button(app,text="4",font='Arial 20')
btn4.place(x=10,y=110,width=40,height=40)

btn5=Button(app,text="5",font='Arial 20')
btn5.place(x=60,y=110,width=40,height=40)

btn6=Button(app,text="6",font='Arial 20')
btn6.place(x=110,y=110,width=40,height=40)

btn7=Button(app,text="7",font='Arial 20')
btn7.place(x=10,y=160,width=40,height=40)

btn8=Button(app,text="8",font='Arial 20')
btn8.place(x=60,y=160,width=40,height=40)

btn9=Button(app,text="9",font='Arial 20')
btn9.place(x=110,y=160,width=40,height=40)

btn0=Button(app,text="0",font='Arial 20')
btn0.place(x=40,y=210,width=40,height=40)

btnt=Button(app,text=".",font='Arial 20')
btnt.place(x=90,y=210,width=40,height=40)


btna=Button(app,text="+",font='Arial 20')
btna.place(x=190,y=60,width=40,height=40)

btns=Button(app,text="-",font='Arial 20')
btns.place(x=240,y=60,width=40,height=40)

btnd=Button(app,text="/",font='Arial 20')
btnd.place(x=190,y=110,width=40,height=40)

btnm=Button(app,text="*",font='Arial 20')
btnm.place(x=240,y=110,width=40,height=40)

btne=Button(app,text="=",font='Arial 20',bg="green")
btne.place(x=190,y=210,width=90,height=40)

btnc=Button(app,text="C",font='Arial 20',bg="red")
btnc.place(x=190,y=160,width=90,height=40)



#обработчики

def press1(event):
    global s
    global digit
    nex()
    s=pole.get()
  
    if s=='0':
        s='1'
    else:
        if len(pole.get())<digit+1:
            s=pole.get()+'1'
    update()
    pushx()

def press2(event):
    global s
    global digit
    nex()
    s=pole.get()
    
    if s=='0':
        s='2'
    else:
        if len(pole.get())<digit+1:
            s=pole.get()+'2'
    update()
    pushx()

def press3(event):
    global s
    global digit
    nex()
    s=pole.get()
   
    if s=='0':
        s='3'
    else:
        if len(pole.get())<digit+1:
            s=pole.get()+'3'
    update()
    pushx()


def press4(event):
    global s
    global digit
    nex()
    s=pole.get()
   
    if s=='0':
        s='4'
    else:
        if len(pole.get())<digit+1:
            s=pole.get()+'4'
    update()
    pushx()

def press5(event):
    global s
    global digit
    nex()
    s=pole.get()
    
    if s=='0':
        s='5'
    else:
        if len(pole.get())<digit+1:
            s=pole.get()+'5'
    update()
    pushx()

def press6(event):
    global s
    global digit
    nex()
    s=pole.get()
    
    if s=='0':
        s='6'
    else:
        if len(pole.get())<digit+1:
            s=pole.get()+'6'
    update()
    pushx()

def press7(event):
    global s
    global digit
    nex()
    s=pole.get()
    
    if s=='0':
        s='7'
    else:
        if len(pole.get())<digit+1:
            s=pole.get()+'7'
    update()
    pushx()

def press8(event):
    global s
    global digit
    nex()
    s=pole.get()
   
    if s=='0':
        s='8'
    else:
        if len(pole.get())<digit+1:
            s=pole.get()+'8'
    update()
    pushx()

def press9(event):
    global s
    global digit
    nex()
    s=pole.get()
    
    if s=='0':
        s='9'
    else:
        if len(pole.get())<digit+1:
            s=pole.get()+'9'
    update()
    pushx()

def press0(event):
    global s
    global digit
    nex()
    s=pole.get()
    
    if s=='0':
        s='0'
    else:
        if len(pole.get())<digit+1:
            s=pole.get()+'0'
    update()
    pushx()


def presst(event):
    global s
    global digit
    nex()
    s=pole.get()
    
    if s=='0':
        s='0.'
    else:
        if len(pole.get())<digit and ('.' not in s):
            s=pole.get()+'.'
    update()
    pushx()

def pressc(event):
    global s
    global digit
    global x
    global y
    global z
    x=0
    y=0
    z=0
    op='0'
    s='0'
    update()


def pressa(event):
    global s
    global x
    global y
    global z
    global op
    global new
    y=x
    op='a'
    new=True
    

def presss(event):
    global s
    global x
    global y
    global z
    global op
    global new
    y=x
    op='s'
    new=True

def pressd(event):
    global s
    global x
    global y
    global z
    global op
    global new
    y=x
    op='d'
    new=True

def pressm(event):
    global s
    global x
    global y
    global z
    global op
    global new
    y=x
    op='m'
    new=True

def presse(event):
    global s
    global x
    global y
    global z
    global op
    global new
    new=True

    if op=='a':
        x=y+x
    if op=='s':
        x=y-x
    if op=='d':
        if x==0:
            s='error'
            update()
            return
        else:
            x=y/x
    if op=='m':
        x=y*x
    op='e'
    showx()
    

def pushx():
    global s
    global x
    x=float(s)

def nex():
    global s
    global new
    
    if new==True:
        s='0'
        update()
        new=False

#привязка нажатий кнопок мышью
        
btn1.bind("<1>",press1)
btn2.bind("<1>",press2)
btn3.bind("<1>",press3)
btn4.bind("<1>",press4)
btn5.bind("<1>",press5)
btn6.bind("<1>",press6)
btn7.bind("<1>",press7)
btn8.bind("<1>",press8)
btn9.bind("<1>",press9)
btn0.bind("<1>",press0)
btnt.bind("<1>",presst)


btna.bind("<1>",pressa)
btns.bind("<1>",presss)
btnd.bind("<1>",pressd)
btnm.bind("<1>",pressm)
btne.bind("<1>",presse)
btnc.bind("<1>",pressc)

#привязка клавиатурных клавиш
app.bind("1",press1)
app.bind("2",press2)
app.bind("3",press3)
app.bind("4",press4)
app.bind("5",press5)
app.bind("6",press6)
app.bind("7",press7)
app.bind("8",press8)
app.bind("9",press9)
app.bind("0",press0)
app.bind(".",presst)


app.bind("+",pressa)
app.bind("-",presss)
app.bind("/",pressd)
app.bind("*",pressm)
app.bind("=",presse)
app.bind("<KeyPress-Return>",presse)
app.bind("<KeyPress-Escape>",pressc)






def showx():
    global x
    global s
    if (x-int(x))==0:
        s=str(int(x))
    else:
        s=str(x)
    update()

def update():
    global s
    pole['state']='normal'
    pole.delete(0,END)
    pole.insert(0,s)
    pole['state']='readonly'

showx()


app.mainloop()
