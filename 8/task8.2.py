#coding=utf-8
from Tkinter import *
from PIL import Image,ImageTk
import tkFileDialog

root=Tk()
root.title('Canvas')

# глобальные переменые
mode='line'  #тип фигуры
color='#000000' # цвет линии
width=1  # толщина линии
fill='#ffffff' # цвет заливки
# списки кнопок цвета линии, толщины, цвета заливки,вида фигур
col=[]
w=[]
f=[]
mod=[]

# координаты начала и конца 
x1=None
x2=None
y1=None
y2=None

draw=False  # флаг рисования
temp=None  # идентификатор для временной фигуры
cursor='plus' # курсор canvasa
ps=None

#print x1,x2,y1,y2

def mouse_down(e): #обработка нажатия кнопки мыши
    global x1,y1,draw,c
    draw=True
    x1=e.x
    y1=e.y
   

def mouse_up(e): #обработка отпускания кнопки мыши
    global mode,x1,y1,x2,y2,draw,c,color,fill
    draw=False
    x2=e.x
    y2=e.y
    if mode=='line':
        c.create_line(x1,y1,x2,y2,fill=color,width=width)
    if mode=='rect':
        c.create_rectangle(x1,y1,x2,y2,outline=color,width=width,fill=fill)
    if mode=='oval':
        c.create_oval(x1,y1,x2,y2,outline=color,width=width,fill=fill)

def mouse_movie(e):  #обработка перемещений мыши (отрисовка промежуточных фигур)
    global mode,x1,y1,draw,c,temp,color,width,fill
    if temp != None:
        c.delete(temp)
    if draw:
        if mode=='line':
            temp=c.create_line(x1,y1,e.x,e.y,fill=color,width=width)
        if mode=='rect':
            temp=c.create_rectangle(x1,y1,e.x,e.y,outline=color,width=width,fill=fill)
        if mode=='oval':
            temp=c.create_oval(x1,y1,e.x,e.y,outline=color,width=width,fill=fill)
        if mode=='curve':
            c.create_line(x1,y1,e.x,e.y,fill=color,width=width)
            x1=e.x
            y1=e.y
        if mode=='lastic':
            c.create_line(x1,y1,e.x,e.y,fill='#ffffff',width=20)
            x1=e.x
            y1=e.y
    


def sw_mode(m):  #переключение режимов (виды фигур)
    global mode,label,width,color,cursor,mod
    for item in mod:
        item.config(bd=0)
    if m=='o':
        mode='oval'
        mod[2].config(bd=3)
        c.config(cursor='plus')
    if m=='r':
        mode='rect'
        mod[1].config(bd=3)
        c.config(cursor='plus')
    if m=='l':
        mode='line'
        mod[0].config(bd=3)
        c.config(cursor='plus')
    if m=='c':
        mode='curve'
        mod[3].config(bd=3)
        c.config(cursor='pencil')
    if m=='ls':
        mode='lastic'
        mod[4].config(bd=3)
        c.config(cursor='circle')


def set_color(c):  #переключение цвета
    global color,col
    color=c
    for item in col:
        if item['bg']==color:
            item.config(bd=3)
        else:
            item.config(bd=0)
    
def set_width(wd): #переключение толщины
    global width,w
    width=wd
    for item in w:
        item.config(bd=0)
    w[wd-1].config(bd=3)


def set_fill(c):
    global fill,f
    fill=c
    for item in f:
        if item['bg']==fill:
            item.config(bd=3)
        else:
            item.config(bd=0)


def save():
    global c,ps
    filename=tkFileDialog.SaveAs(root,filetypes=[('post script files','.ps')]).show()
    if filename=='':
        return
    if not filename.endswith('.ps'):
        filename+='.ps'
    c.postscript(file=filename,colormode ='color')

def load():
    global c
    

def clear_all():
    c.delete('all')
    
# Canvas
c=Canvas(root,width=480,height=360,cursor=cursor,bg='#ffffff',bd=3)
c.pack()

#кнопки переключения фигур

frm_mode=Frame(root)
frm_mode.pack(expand=1,fill='both')

label_mode=Label(frm_mode,text='Фигура:',font='Arial 16')
label_mode.pack(side='left')

mod.append(Button(frm_mode,text='line',width=7,font='Arial 16',command=lambda m='l': sw_mode(m)))
mod[len(mod)-1].pack(side='left')

mod.append(Button(frm_mode,text='rect',width=7,font='Arial 16',command=lambda m='r': sw_mode(m)))
mod[len(mod)-1].pack(side='left')

mod.append(Button(frm_mode,text='oval',width=7,font='Arial 16',command=lambda m='o': sw_mode(m)))
mod[len(mod)-1].pack(side='left')

mod.append(Button(frm_mode,text='curve',width=7,font='Arial 16',command=lambda m='c': sw_mode(m)))
mod[len(mod)-1].pack(side='left')

mod.append(Button(frm_mode,text='lastic',width=7,font='Arial 16',command=lambda m='ls': sw_mode(m)))
mod[len(mod)-1].pack(side='left')


# кнопки переключения цвета
frm_color=Frame(root)
frm_color.pack(expand=1,fill='both')

label_color=Label(frm_color,text='Цвет линии:',font='Arial 16')
label_color.pack(side='left')

col.append(Button(frm_color,width=2,bg='#ff0000',command=lambda c='#ff0000':set_color(c)))
col[len(col)-1].pack(side='right')

col.append(Button(frm_color,width=2,bg='#00ff00',command=lambda c='#00ff00':set_color(c)))
col[len(col)-1].pack(side='right')

col.append(Button(frm_color,width=2,bg='#0000ff',command=lambda c='#0000ff':set_color(c)))
col[len(col)-1].pack(side='right')

col.append(Button(frm_color,width=2,bg='#000000',command=lambda c='#000000':set_color(c)))
col[len(col)-1].pack(side='right')

col.append(Button(frm_color,width=2,bg='#ffffff',command=lambda c='#ffffff':set_color(c)))
col[len(col)-1].pack(side='right')


# кнопки переключения цвета заливки
frm_fill=Frame(root)
frm_fill.pack(expand=1,fill='both')

label_fill=Label(frm_fill,text='Цвет заливки:',font='Arial 16')
label_fill.pack(side='left')

f.append(Button(frm_fill,width=2,bg='#ff0000',command=lambda c='#ff0000':set_fill(c)))
f[len(f)-1].pack(side='right')

f.append(Button(frm_fill,width=2,bg='#00ff00',command=lambda c='#00ff00':set_fill(c)))
f[len(f)-1].pack(side='right')

f.append(Button(frm_fill,width=2,bg='#0000ff',command=lambda c='#0000ff':set_fill(c)))
f[len(f)-1].pack(side='right')

f.append(Button(frm_fill,width=2,bg='#000000',command=lambda c='#000000':set_fill(c)))
f[len(f)-1].pack(side='right')

f.append(Button(frm_fill,width=2,bg='#ffffff',command=lambda c='#ffffff':set_fill(c)))
f[len(f)-1].pack(side='right')


# кнопки переключения толщины
frm_width=Frame(root)
frm_width.pack(expand=1,fill='both')

label_width=Label(frm_width,text='Толщина линии:',font='Arial 16')
label_width.pack(side='left')

w.append(Button(frm_width,width=2,text='1',command=lambda w=1:set_width(w)))
w[len(w)-1].pack(side='right')

w.append(Button(frm_width,width=2,text='2',command=lambda w=2:set_width(w)))
w[len(w)-1].pack(side='right')

w.append(Button(frm_width,width=2,text='3',command=lambda w=3:set_width(w)))
w[len(w)-1].pack(side='right')

w.append(Button(frm_width,width=2,text='4',command=lambda w=4:set_width(w)))
w[len(w)-1].pack(side='right')

w.append(Button(frm_width,width=2,text='5',command=lambda w=5:set_width(w)))
w[len(w)-1].pack(side='right')


Button(root,text='Сохранить',font='Arial 16',command=save).pack(side='left')
Button(root,text='Очистить',font='Arial 16',command=clear_all).pack(side='left')



# привязка событий мыши
c.bind("<ButtonPress-1>",mouse_down)
c.bind("<ButtonRelease-1>",mouse_up)
c.bind("<Motion>",mouse_movie)

# инициализация начального состояния
set_color('#000000')
set_width(1)
set_fill('#ffffff')
sw_mode('l')

root.mainloop()
