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

btn1=Button(app,text="1",font='Arial 20', command=lambda p='1':press(p))
btn1.place(x=10,y=60,width=40,height=40)


btn2=Button(app,text="2",font='Arial 20', command=lambda p='2':press(p))
btn2.place(x=60,y=60,width=40,height=40)

btn3=Button(app,text="3",font='Arial 20', command=lambda p='3':press(p))
btn3.place(x=110,y=60,width=40,height=40)

btn4=Button(app,text="4",font='Arial 20', command=lambda p='4':press(p))
btn4.place(x=10,y=110,width=40,height=40)

btn5=Button(app,text="5",font='Arial 20', command=lambda p='5':press(p))
btn5.place(x=60,y=110,width=40,height=40)

btn6=Button(app,text="6",font='Arial 20', command=lambda p='6':press(p))
btn6.place(x=110,y=110,width=40,height=40)

btn7=Button(app,text="7",font='Arial 20', command=lambda p='7':press(p))
btn7.place(x=10,y=160,width=40,height=40)

btn8=Button(app,text="8",font='Arial 20', command=lambda p='8':press(p))
btn8.place(x=60,y=160,width=40,height=40)

btn9=Button(app,text="9",font='Arial 20', command=lambda p='9':press(p))
btn9.place(x=110,y=160,width=40,height=40)

btn0=Button(app,text="0",font='Arial 20', command=lambda p='0':press(p))
btn0.place(x=40,y=210,width=40,height=40)

btnt=Button(app,text=".",font='Arial 20')
btnt.place(x=90,y=210,width=40,height=40)


btna=Button(app,text="+",font='Arial 20',command=lambda o='a':oper(o))
btna.place(x=190,y=60,width=40,height=40)

btns=Button(app,text="-",font='Arial 20',command=lambda o='s':oper(o))
btns.place(x=240,y=60,width=40,height=40)

btnd=Button(app,text="/",font='Arial 20',command=lambda o='d':oper(o))
btnd.place(x=190,y=110,width=40,height=40)

btnm=Button(app,text="*",font='Arial 20',command=lambda o='m':oper(o))
btnm.place(x=240,y=110,width=40,height=40)

btne=Button(app,text="=",font='Arial 20',bg="green")
btne.place(x=190,y=210,width=90,height=40)

btnc=Button(app,text="C",font='Arial 20',bg="red")
btnc.place(x=190,y=160,width=90,height=40)



#обработчики

def press(p):
    global s
    global digit
    nex()
    s=pole.get()
  
    if s=='0':
        s=p
    else:
        if len(pole.get())<digit+1:
            s=pole.get()+p
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



def oper(o):
    global s
    global x
    global y
    global z
    global op
    global new
    y=x
    op=o
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
    #print s
    x=float(s)

def nex():
    global s
    global new
    
    if new==True:
        s='0'
        update()
        new=False



def reportEvent(event):
        #print event.keysym
        
        if event.keysym=='1':
            press('1')
        if event.keysym=='2':
            press('2')
        if event.keysym=='3':
            press('3')
        if event.keysym=='4':
            press('4')
        if event.keysym=='5':
            press('5')
        if event.keysym=='6':
            press('6')
        if event.keysym=='7':
            press('7')
        if event.keysym=='8':
            press('8')
        if event.keysym=='9':
            press('9')
        if event.keysym=='0':
            press('0')
        if event.keysym=='plus':
            oper('a')
        if event.keysym=='minus':
            oper('s')
        if event.keysym=='slash':
            oper('d')
        if event.keysym=='asterisk':
            oper('m')



            

#привязка нажатий кнопок мышью
        

btnt.bind("<1>",presst)
btne.bind("<1>",presse)
btnc.bind("<1>",pressc)

#привязка клавиатурных клавиш

app.bind("<KeyPress>",reportEvent)

app.bind(".",presst)



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
