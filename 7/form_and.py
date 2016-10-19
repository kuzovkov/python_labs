#coding=utf-8
from Tkinter import *
from test import *

root=Tk()
root.geometry('640x480')
root.title('Вопрос and')

i=4

result={}

def send():
    global cbvar
    global result
    rsp_ls=[]
    for ch in cbvar:
        rsp_ls.append(ch.get())
    rsp=tuple(rsp_ls)

    if rsp==responses_and[i]:
        result.update({i:True})
    else:
        result.update({i:False})
    
    

    print result  
    

number=Label(root,text='Вопрос '+str(i)+' из '+str(len(questions))).pack()
question=Label(root,text=questions[i],bg='#ffffff',width=100,height=10).pack()



cbvar=[]
check=[]

for item in variants[i]:
    ch=IntVar()
    cbvar.append(ch)
    cb=Checkbutton(root,text=item,variable=cbvar[len(cbvar)-1],onvalue=1,offvalue=0)
    check.append(cb)
    check[len(check)-1].pack()


  




next_btn=Button(root,text='Отправить ответ', font='Arial 20', command=send).pack()

root.mainloop()

