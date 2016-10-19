#coding=utf-8
from Tkinter import *
import tkMessageBox
from time import localtime,asctime
from test import *

root=Tk()
root.geometry('640x480')
root.title('End')



result={1:True,2:False,3:False,4:False,5:False,6:True}
name='Иван'

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
    #выход из программы
    endtest=tkMessageBox.askokcancel("Тест","Точно выйти?")
    if endtest:
        root.destroy()

def new():
    pass

#подсчет правильных ответов и процентов
right=0
for i in result.values():
    if i:
        right=right+1

percent=int(100*float(right)/len(questions))

#расчет оценки
if right>=head['norma5']:
    itog="Отлично"
    itogfg="#0000ff"
else:
    if right>=head['norma4']:
        itog="Хорошо"
        itogfg="#00ff00"
    else:
        if right>=head['norma3']:
            itog="Удовлетворительно"
            itogfg="#ff00ff"
        else:
            itog="Неудовлетворительно"
            itogfg="#ff0000"


end_name_test=Label(root,text=head['name'],font='Arial 20', bg='#666666',fg='#0000ff',width=40,height=3).pack()
end_title=Label(root,text='Результаты тестирования',font='Arial 18 bold',bg='#fff',fg='#ff0000',width=40).pack()
end_name=Label(root,text='Имя: '+name,bg='#fff',width=100,height=2,font='Arial 14').pack()
number_questions=Label(root,text='Количество вопросов в тесте: '+str(len(questions)),font='Arial 14',bg='#fff',width=100).pack()
number_right=Label(root,text='Правильных ответов: '+str(right),bg='#fff',width=100,font='Arial 14').pack()
percent_right=Label(root,text='Процент правильных ответов: '+str(percent)+" %",bg='#fff',width=40,font='Arial 14').pack()

testitog=Label(root,text='Результат тестирования: ',bg='#fff',width=40,font='Arial 14').pack()
testitog2=Label(root,text=itog,width=40,fg=itogfg,font='Arial 14').pack()



#кнопки
start_btn=Button(root,text='Повторить тестирование', font='Arial 20', command=start).pack()
reapeat_btn=Button(root,text='Новый пользователь', font='Arial 20', command=new).pack()
end_btn=Button(root,text='Выход', font='Arial 20', command=end).pack()

#запись результатов в файл
f=open("results.txt","a+")
res="*"*60+"\nНазвание теста: "+head['name']+"\nИмя: "+name
res=res+"\nКоличество вопросов: "+str(len(questions))
res=res+"\nКоличество правильных ответов: "+str(right)
res=res+"\nПроцент правильных ответов: "+str(percent)
res=res+"\nРезультат тестирования: "+itog
res=res+"\nВремя: "+asctime(localtime())+"\n"

f.write(res)
f.close()



root.mainloop()

