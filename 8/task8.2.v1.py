#coding=utf-8
from Tkinter import *
from PIL import Image,ImageTk

root=Tk()
root.title('Canvas')

mode='line'
color='#000000'
width=1
col=[]
w=[]

x1=None
x2=None
y1=None
y2=None

draw=False
temp=None
cursor='plus'

#print x1,x2,y1,y2

def mouse_down(e): #обработка нажатия кнопки мыши
    global x1,y1,draw,c
    draw=True
    x1=e.x
    y1=e.y
   

def mouse_up(e): #обработка отпускания кнопки мыши
    global mode,x1,y1,x2,y2,draw,c,color
    draw=False
    x2=e.x
    y2=e.y
    if mode=='line':
        c.create_line(x1,y1,x2,y2,fill=color,width=width)
    if mode=='rect':
        c.create_rectangle(x1,y1,x2,y2,outline=color,width=width)
    if mode=='oval':
        c.create_oval(x1,y1,x2,y2,outline=color,width=width)

def mouse_movie(e):  #обработка перемещений мыши (отрисовка промежуточных фигур)
    global mode,x1,y1,draw,c,temp,color,width
    if temp != None:
        c.delete(temp)
    if draw:
        if mode=='line':
            temp=c.create_line(x1,y1,e.x,e.y,fill=color,width=width)
        if mode=='rect':
            temp=c.create_rectangle(x1,y1,e.x,e.y,outline=color,width=width)
        if mode=='oval':
            temp=c.create_oval(x1,y1,e.x,e.y,outline=color,width=width)
        if mode=='curve':
            c.create_line(x1,y1,e.x,e.y,fill=color,width=width)
            x1=e.x
            y1=e.y
        if mode=='lastic':
            c.create_line(x1,y1,e.x,e.y,fill='#ffffff',width=20)
            x1=e.x
            y1=e.y
    


def sw_mode(m):  #переключение режимов (виды фигур)
    global mode,label,width,color,cursor
    if m=='o':
        mode='oval'
        label.configure(text='oval')
        c.config(cursor='plus')
    if m=='r':
        mode='rect'
        label.configure(text='rect')
        c.config(cursor='plus')
    if m=='l':
        mode='line'
        label.configure(text='line')
        c.config(cursor='plus')
    if m=='c':
        mode='curve'
        label.configure(text='curve')
        c.config(cursor='pencil')
    if m=='ls':
        mode='lastic'
        label.configure(text='lastic')
        c.config(cursor='circle')


def set_color(c):  #переключение цвета
    global color,col
    color=c
    for item in col:
        item.config(bd=0)
    for item in col:
        if item['bg']==color:
            item.config(bd=3)
    
def set_width(wd): #переключение толщины
    global width,w
    width=wd
    for item in w:
        item.config(bd=0)
    w[wd-1].config(bd=3)


    

c=Canvas(root,width=480,height=360,cursor=cursor,bg='#ffffff',bd=3)
c.pack()


bt_line=Button(root,text='line',font='Arial 16',command=lambda m='l': sw_mode(m))
bt_line.pack(side='left')

bt_rect=Button(root,text='rect',font='Arial 16',command=lambda m='r': sw_mode(m))
bt_rect.pack(side='left')

bt_oval=Button(root,text='oval',font='Arial 16',command=lambda m='o': sw_mode(m))
bt_oval.pack(side='left')

bt_oval=Button(root,text='curve',font='Arial 16',command=lambda m='c': sw_mode(m))
bt_oval.pack(side='left')

Button(root,text='lastic',font='Arial 16',command=lambda m='ls': sw_mode(m)).pack(side='left')

label=Label(root,width=7,text='line',font='Arial 16')
label.pack(side='right')


col.append(Button(root,width=2,bg='#ff0000',command=lambda c='#ff0000':set_color(c)))
col[len(col)-1].pack(side='right')
col.append(Button(root,width=2,bg='#00ff00',command=lambda c='#00ff00':set_color(c)))
col[len(col)-1].pack(side='right')
col.append(Button(root,width=2,bg='#0000ff',command=lambda c='#0000ff':set_color(c)))
col[len(col)-1].pack(side='right')
col.append(Button(root,width=2,bg='#000000',command=lambda c='#000000':set_color(c)))
col[len(col)-1].pack(side='right')


w.append(Button(root,width=2,text='1',command=lambda w=1:set_width(w)))
w[len(w)-1].pack(side='right')
w.append(Button(root,width=2,text='2',command=lambda w=2:set_width(w)))
w[len(w)-1].pack(side='right')
w.append(Button(root,width=2,text='3',command=lambda w=3:set_width(w)))
w[len(w)-1].pack(side='right')
w.append(Button(root,width=2,text='4',command=lambda w=4:set_width(w)))
w[len(w)-1].pack(side='right')





c.bind("<ButtonPress-1>",mouse_down)
c.bind("<ButtonRelease-1>",mouse_up)
c.bind("<Motion>",mouse_movie)
set_color('#000000')


root.mainloop()
