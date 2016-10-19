#coding=utf-8
from Tkinter import *
from test import *

root=Tk()
root.geometry('800x600')
root.title('Вопрос or')

i=2

result={}

def send():
    global rbvar
    global result
    
    if responses_or[i]==rbvar.get():
        result.update({i:True})
    else:
        result.update({i:False})

    #print result  
    

number=Label(root,text='Вопрос '+str(i)+' из '+str(len(questions))).pack()
question=Label(root,text=questions[i],bg='#fff',width=100,height=30).pack()


rbvar=IntVar()
rbvar.set(1)


    

rbts=[]
j=1
for item in variants[i]:
    rb=Radiobutton(root,text=item,variable=rbvar,value=j)
    rbts.append(rb)
    rbts[len(rbts)-1].pack()
    j=j+1
  




next_btn=Button(root,text='Отправить ответ', font='Arial 20', command=send).pack()

root.mainloop()
