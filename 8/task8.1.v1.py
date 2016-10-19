#coding=utf=8
from Tkinter import *
import tkMessageBox
from PIL import Image,ImageTk
from time import *


filename='files.txt'
i=0
frm=None
img=None
btn_pause=None
pause=False
text_btn_pause='Pause'
    

root=Tk()
root.title('Слайдер')

def sw_pause():
    global pause,text_btn_pause
    if not pause:
        pause=True
    else:
        pause=False
    if pause:
        text_btn_pause='Start'
        btn_pause.configure(text=text_btn_pause)
    else:
        text_btn_pause='Pause'
        btn_pause.configure(text=text_btn_pause)
        
def clear_frame():
    global frm
    frm.destroy()
    
def next_image():
    global i
    if i < len(files_ls)-1:
        i=i+1
        show_image(i)
    else:
        i=0
        show_image(i)

def prev_image():
    global i
    if i >0:
        i=i-1
        show_image(i)
    else:
        i=len(files_ls)-1
        show_image(i)

def show_image(k):
    global files_ls,frm,img,pause,btn_pause

    if frm != None:
        clear_frame()
    
    frm=Frame(root,bg='#ffffff')
    frm.pack(expand=1,fill='both')
    #print i,k,files_ls[i]
    src=Image.open(files_ls[k])
    img=ImageTk.PhotoImage(src)
    Button(frm,text='Next >',font='Arial 20',bg='#ff0000',command=next_image).pack(side='right')
    Button(frm,text='< Prev',font='Arial 20',bg='#ff0000',command=prev_image).pack(side='left')
    label=Label(frm,image=img)
    label.pack()
    Label(frm,text=files_ls[k],font='Arial 16',bg='#ffffff').pack()
    
    btn_pause=Button(frm,text=text_btn_pause, font='Arial 20',bg='#ff0000',command=sw_pause)
    btn_pause.pack(side='bottom')
    


def auto():
    global pause
    root.after(3000,auto)
    if not pause:
        next_image()


    

try:
    f=open(filename,'r')
except IOError:
    tkMessageBox.showwarning('Слайдер','Не могу открыть файл '+filename)
else:
    files=f.read()
    files_ls=files.split('\n')
    root.after(3000,auto)

    show_image(0)
    
root.mainloop()
