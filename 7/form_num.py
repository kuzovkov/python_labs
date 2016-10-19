#coding=utf-8
from Tkinter import *
from test import *

root=Tk()
root.geometry('800x600')
root.title('Вопрос num')

i=5

result={}

def send():
    global rsp_text
    global result

   
    if rsp_text.get()==str(responses_num[i]):
        result.update({i:True})
    else:
        result.update({i:False})
    

    print result  
    

number=Label(root,text='Вопрос '+str(i)+' из '+str(len(questions))).pack()
question=Label(root,text=questions[i],bg='#fff',width=100,height=30).pack()

rsp_text=StringVar()

pole_num=Entry(root,width=30,font='Arial 14',textvariable=rsp_text).pack()


next_btn=Button(root,text='Отправить ответ', font='Arial 20', command=send).pack()

root.mainloop()


