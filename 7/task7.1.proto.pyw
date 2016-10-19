#coding=utf-8
#Кузовков Александр Владимирович

from Tkinter import *;
from test import *;

root=Tk()

root.title("Тест "+head['name'])
root.geometry('640x480');
#root.resizable(0,0)

frm=None

bg1="#fee"
bg2="#fff"

def start():
    global questions
    for i in questions.keys():
        clear_frame()

def clear_frame():
    global frm
    frm.destroy()
    print type(frm)
def draw_frame(p):
    global frm
    global head,questions

    
    frm=Frame(root,bg=bg2,bd=10)
    frm.pack(expand=1,fill="both")

    t_name=Label(frm,text=head['name'],font='Arial 20',bg=bg2)
    t_name.pack(expand=1,fill="both")

    t_rules=Label(frm,text=head['rules'],font='Arial 12',bg=bg2)
    t_rules.pack(expand=1,fill="both")

    
    t_invite=Label(frm,text='Для начала тестирования введите Ваше имя', font='Arial 12',bg=bg2)
    t_invite.pack(expand=1,fill="both", side="left")

    e_name=Entry(frm)
    e_name.pack(expand=1,side="right")
    
    btn_exit=Button(frm,text="exit",command=lambda:root.destroy())
    btn_exit.pack()
   
     
    btn_clr=Button(frm,text="clr",command=start)
    btn_clr.pack()


#print quest

draw_frame(0)

root.mainloop()

