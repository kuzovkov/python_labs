#coding=utf-8
from Tkinter import *
import tkMessageBox
from time import localtime,asctime
from test import *


root=Tk()
root.geometry('640x480')
root.title('Тест - '+head['name'])

#глобальные переменные
result={}
name=''
user_name=StringVar()
frm=None

#функции
#начало теста
def start():
    global user_name
    global name
    
    if len(user_name.get())>0 and user_name.get().isalpha():
        name=user_name.get()
        print name
    else:
        user_name.set('')
        print "False"
    
# выход из программы
def end():

    endtest=tkMessageBox.askokcancel("Тест","Точно выйти?")
    if endtest:
        root.destroy()

def close():
    global frm
    frm.destroy()

def show_start():
    global frm
    global head
    global questions
    global end
    global start
    global user_name
    
    frm=Frame(root,bg='#dddddd').pack(expand=1,fill="both")

    test_name=Label(frm,text=head['name'],font='Arial 20', bg='#ffffff',width=40).pack()
    rules=Label(frm,text=head['rules'],bg='#fff',width=100,height=10).pack()
    number_questions=Label(frm,text='Количество вопросов в тесте: '+str(len(questions)),bg='#fff',width=100).pack()
    number_min=Label(frm,text='Минимум правильных ответов: '+str(head['norma3']),bg='#fff',width=100).pack()
    invite=Label(frm,text='Для начала тестирования введите Ваше имя: ',bg='#fff',width=40).pack()


    pole=Entry(frm,width=30,font='Arial 14',textvariable=user_name).pack()


    next_btn=Button(frm,text='Начать тестирование', font='Arial 20', command=start).pack()
    end_btn=Button(frm,text='Выход', font='Arial 20', command=end).pack()


show_start()

root.mainloop()
