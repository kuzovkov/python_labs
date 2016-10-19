#coding=utf-8
from Tkinter import *
import tkMessageBox
from test import *

root=Tk()
root.geometry('640x480')
root.title('Start')



result={}
name=''

def start():
    global user_name
    global name
    
    if len(user_name.get())>0 and user_name.get().isalpha():
        name=user_name.get()
        print name
    else:
        user_name.set('')
        print "False"
    
def end():

    endtest=tkMessageBox.askokcancel("Тест","Точно выйти?")
    if endtest:
        root.destroy()



test_name=Label(root,text=head['name'],font='Arial 20', bg='#ffffff',width=40).pack()
rules=Label(root,text=head['rules'],bg='#fff',width=100,height=10).pack()
number_questions=Label(root,text='Количество вопросов в тесте: '+str(len(questions)),bg='#fff',width=100).pack()
number_min=Label(root,text='Минимум правильных ответов: '+str(head['norma3']),bg='#fff',width=100).pack()
invite=Label(root,text='Для начала тестирования введите Ваше имя: ',bg='#fff',width=40).pack()

user_name=StringVar()

pole=Entry(root,width=30,font='Arial 14',textvariable=user_name).pack()


next_btn=Button(root,text='Начать тестирование', font='Arial 20', command=start).pack()
end_btn=Button(root,text='Выход', font='Arial 20', command=end).pack()

root.mainloop()

