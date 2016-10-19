#coding=utf-8
from Tkinter import *
import tkMessageBox
from time import localtime,asctime
from test import *


root=Tk()
root.geometry('640x480')
root.title('Тест - '+head['name'])
root.resizable(0,0)

#глобальные переменные
frm=None
result={}
name=''
user_name=StringVar()
i=0
rsp_text=StringVar()
rbvar=IntVar()
cbvar=[]

#цвета

white='#ffffff'
red='#ff0000'
red1='#ae1422'
red2='#f24757'
red3='#e214cc'
green='#00ff00'
green1='#1bb50b'
green2='#afe6aa'
green3='#127208'
blue='#0000ff'
blue1='#2480f2'
blue2='#0e3769'
blue3='#609fed'
yellow='#e7e712'
yellow1='#f2be12'
yellow2='#d49512'
yellow3='#e2ee12'

grey='#eeeeee'
grey1='#cccccc'
grey2='#aaaaaa'
grey3='#666666'
grey4='#333333'
black='#000000'

# фон формы
bg1=grey

# фон поля вопроса
bg2=white

# фон поля правил
bg3=grey1

# фон кнопки далее
bg4=green1

# фон кнопки выхода
bg5=red
# фон кнопки повтора
bg6=yellow2

#цвет названия теста
fg1=red3

#цвет вопросов
fg2=black

#цвет правил
fg3=green3

#цвет ответов
fg4=black

#цвет результата теста
fg5=green3

#цвет количества вопросов
fg6=green2

#цвет текста на кнопках
fg7=white



#функции
#начало теста
def start(e=0):
    global user_name,name,questions,i
    
    if len(user_name.get())>0 and user_name.get().isalpha():  #если имя введено корректно
        name=user_name.get()
        result.clear()
        select_form() #выбираем форму для первого вопроса 
    else:
        user_name.set('')
        tkMessageBox.showwarning("Тест","Вы не ввели имя или имя содержит символы кроме букв")

def start_again(e=0):
    global frm
    
    clear_frame()
    result.clear()
    start()



def new_user(e=0):
    global frm

    clear_frame()
    result.clear()
    show_start()

    

def select_form(e=0):  #увеличение индекса и выбор формы для показа
    global user_name,name,questions,i

    clear_frame()

    i=i+1
    if i > len(questions):
        show_form_end()
    else:
        if responses_str.has_key(i):
            show_form_str()
        else:
            if responses_num.has_key(i):
                show_form_num()
            else:
                if responses_and.has_key(i):
                    show_form_and()
                else:
                    if responses_or.has_key(i):
                        show_form_or()
                        
            
    
# выход из программы
def end2(e=0):

    endtest=tkMessageBox.askokcancel("Тест","Точно выйти?")
    if endtest:
        root.destroy()

def end(e=0):

    endtest=tkMessageBox.askokcancel("Тест","Точно выйти? Результаты не будут сохранены")
    if endtest:
        root.destroy()




def clear_frame(): #очистка фрейма
    global frm
    frm.destroy()

def send_str(e=0): #обработка строкового ответа
    global rsp_text,responses_str
    global result,i

    if rsp_text.get()=='':
        if tkMessageBox.askokcancel("Тест","Вы ввели пустую строку, продолжить?"):
            pass
        else:
            clear_frame()
            show_form_str()
            return
    if rsp_text.get().lower()==responses_str[i].decode('utf8'):
        result.update({i:True})
    else:
        result.update({i:False})
    select_form()
    #print result

def send_num(e=0): #обработка числового ответа
    global rsp_text,responses_num
    global result,i

    if not rsp_text.get().isdigit():
        tkMessageBox.showwarning("Тест","Вы ввели не число!")
        clear_frame()
        show_form_num()
        return
    if rsp_text.get()==str(responses_num[i]):
        result.update({i:True})
    else:
        result.update({i:False})
    select_form()
    #print result

def send_and(e=0): #обработка  ответа типа And
    global cbvar,responses_and
    global result,i

    rsp_ls=[]
    for ch in cbvar:
        rsp_ls.append(ch.get())
    rsp=tuple(rsp_ls)

    
    if rsp==responses_and[i]:
        result.update({i:True})
    else:
        result.update({i:False})
    select_form()
    #print result

def send_or(e=0): #обработка  ответа типа Or
    global rbvar,responses_or
    global result,i
    
    if responses_or[i]==rbvar.get():
        result.update({i:True})
    else:
        result.update({i:False})
    select_form()
    #print result


def show_start(): #показ стартовой формы
    global frm,head,questions,user_name
    
    frm=Frame(root,bg=bg1,bd=5)
    frm.pack(expand=1,fill="both")

    test_name=Label(frm,text=head['name'],font='Arial 20', bg=bg1,fg=fg1,width=40).pack()
    rules=Label(frm,text=head['rules'],justify=LEFT,bg=bg1,fg=fg3,width=100,height=10).pack()
    number_questions=Label(frm,text='Количество вопросов в тесте: '+str(len(questions)),font='Arial 14',bg=bg1,fg=fg3,width=100).pack()
    number_min=Label(frm,text='Минимум правильных ответов: '+str(head['norma3']),font='Arial 14',bg=bg1,fg=fg3,width=100).pack()
    invite=Label(frm,text='Для начала тестирования введите Ваше имя: ',font='Arial 14',bg=bg1,fg=fg4,width=40).pack()
    pole=Entry(frm,takefocus=TRUE,bd=5,width=30, font='Arial 14', textvariable=user_name).pack()
    next_btn=Button(frm,pady=3,bd=5,text='Начать тест (Enter)', font='Arial 20',bg=bg4,fg=fg6,width=20, command=start).pack(side='bottom')
    end_btn=Button(frm,pady=3,bd=5,text='Выход (Esc)', width=20,font='Arial 20', bg=bg5,fg=fg6,command=end2).pack(side='bottom')
    root.bind('<KeyPress-Return>',start)
    root.bind('<KeyPress-Escape>',end2)

def show_form_str(): #показ формы строкового ответа
    global i,head,questions,responses_str,frm,rsp_text

    frm=Frame(root,bg=bg1,bd=5)
    frm.pack(expand=1,fill="both")
    
    number=Label(frm,bg=bg1,fg=fg3,text='Вопрос '+str(i)+' из '+str(len(questions))).pack()
    question=Label(frm,bd=5,text=questions[i],bg=bg2,fg=fg2,width=100,height=5).pack()
    pole=Entry(frm,bd=5,width=30,font='Arial 14',textvariable=rsp_text).pack()
    next_btn=Button(frm,bd=5,text='Отправить ответ (Enter)', font='Arial 20', command=send_str,bg=bg4,fg=fg6,width=20).pack(side='bottom')
    end_btn=Button(frm,bd=5,text='Выход (Esc)', font='Arial 20', command=end,bg=bg5,fg=fg6,width=20).pack(side='bottom')
    rsp_text.set('')
    root.bind('<KeyPress-Return>',send_str)
    root.bind('<KeyPress-Escape>',end)

def show_form_num(): #показ формы числового ответа
    global frm,i,rsp_text,questions
    
    frm=Frame(root,bg=bg1,bd=5)
    frm.pack(expand=1,fill="both")
    
    number=Label(frm,bg=bg1,fg=fg3,text='Вопрос '+str(i)+' из '+str(len(questions))).pack()
    question=Label(frm,bd=5,text=questions[i],bg=bg2,fg=fg2,width=100,height=5).pack()
    pole_num=Entry(frm,bd=5,width=30,font='Arial 14',textvariable=rsp_text).pack()
    next_btn=Button(frm,bd=5,text='Отправить ответ (Enter)', bg=bg4,fg=fg6,font='Arial 20',width=20, command=send_num).pack(side='bottom')
    end_btn=Button(frm,bd=5,text='Выход (Esc)', bg=bg5,fg=fg6,font='Arial 20', width=20,command=end).pack(side='bottom')
    rsp_text.set('')
    root.bind('<KeyPress-Return>',send_num)
    root.bind('<KeyPress-Escape>',end)

def show_form_and(): #показ формы  ответа типа And
    global frm,i,questions,cbvar
    
    frm=Frame(root,bg=bg1,bd=5)
    frm.pack(expand=1,fill="both")
    
    number=Label(frm,bg=bg1,fg=fg2,text='Вопрос '+str(i)+' из '+str(len(questions))).pack()
    question=Label(frm,bd=5,bg=bg2,fg=fg2,text=questions[i],width=100,height=5).pack()

    check=[]
    cbvar=[]

    
    for item in variants[i]:
        ch=IntVar()
        cbvar.append(ch)
        cb=Checkbutton(frm,bd=3,bg=bg1,fg=fg2,text=item,variable=cbvar[len(cbvar)-1],onvalue=1,offvalue=0)
        check.append(cb)
        check[len(check)-1].pack()

    next_btn=Button(frm,bd=5,bg=bg4,fg=fg6,text='Отправить ответ (Enter)', font='Arial 20', command=send_and,width=20).pack(side='bottom')
    end_btn=Button(frm,bd=5,bg=bg5,fg=fg6,text='Выход (Esc)', font='Arial 20', command=end,width=20).pack(side='bottom')
    root.bind('<KeyPress-Return>',send_and)
    root.bind('<KeyPress-Escape>',end)

    
def show_form_or():  #показ формы  ответа типа Or
    global frm,i,questions,rbvar,variants
    
    frm=Frame(root,bg=bg1,bd=5)
    frm.pack(expand=1,fill="both")

    
    number=Label(frm,bg=bg1,fg=fg3,text='Вопрос '+str(i)+' из '+str(len(questions))).pack()
    question=Label(frm,bd=5,text=questions[i],bg=bg2,fg=fg2,width=100,height=5).pack()
   
    
    rbvar.set(1)

    rbts=[]
    j=1
    for item in variants[i]:
        rb=Radiobutton(frm,bd=5,bg=bg1,fg=fg2,text=item,variable=rbvar,value=j)
        rbts.append(rb)
        rbts[len(rbts)-1].pack()
        j=j+1
      
    next_btn=Button(frm,bd=5,bg=bg4,fg=fg6,text='Отправить ответ (Enter)', font='Arial 20',width=20, command=send_or).pack(side='bottom')
    end_btn=Button(frm,bd=5,bg=bg5,fg=fg6,text='Выход (Esc)', font='Arial 20',width=20, command=end).pack(side='bottom')
    root.bind('<KeyPress-Return>',send_or)
    root.bind('<KeyPress-Escape>',end)

def show_form_end():  #показ формы  результата
    global result,head,questions,frm,i

    i=0
    #подсчет правильных ответов и процентов
    right=0
    for k in result.values():
        if k:
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


    frm=Frame(root,bg=bg1,bd=5)
    frm.pack(expand=1,fill="both")

    end_name_test=Label(frm,text=head['name'],font='Arial 20', bg=bg1,fg=fg1,width=40,height=2).pack()
    end_title=Label(frm,text='Результаты тестирования',font='Arial 18 bold',bg=bg1,fg=fg5,width=40).pack()
    end_name=Label(frm,text='Имя: '+name.encode('utf8'),bg=bg1,fg=fg3,width=100,height=2,font='Arial 14').pack()
    number_questions=Label(frm,bg=bg1,fg=fg3,text='Количество вопросов в тесте: '+str(len(questions)),font='Arial 14',width=100).pack()
    number_right=Label(frm,bg=bg1,fg=fg3,text='Правильных ответов: '+str(right),width=100,font='Arial 14').pack()
    percent_right=Label(frm,bg=bg1,fg=fg3,text='Процент правильных ответов: '+str(percent)+" %",width=40,font='Arial 14').pack()

    testitog=Label(frm,text='Результат тестирования: ',bg=bg1,fg=fg5,width=40,font='Arial 14').pack()
    testitog2=Label(frm,text=itog,width=40,bg=bg1,fg=itogfg,font='Arial 14').pack()



    #кнопки
    start_btn=Button(frm,bd=5,bg=bg4,fg=fg6,text='Повторить тест (Enter)',width=20, font='Arial 20', command=start_again).pack(side='bottom')
    reapeat_btn=Button(frm,bd=5,bg=bg6,fg=fg6,text='Новый пользователь', width=20,font='Arial 20', command=new_user).pack(side='bottom')
    end_btn=Button(frm,bd=5,bg=bg5,fg=fg6,text='Выход (Esc)', font='Arial 20', command=end2,width=20).pack(side='bottom')
    root.bind('<KeyPress-Return>',start_again)
    root.bind('<KeyPress-Escape>',end2)


    #запись результатов в файл
    f=open("results.txt","a+")
    res="*"*60+"\nНазвание теста: "+head['name']+"\nИмя: "+name.encode('utf8')
    res=res+"\nКоличество вопросов: "+str(len(questions))
    res=res+"\nКоличество правильных ответов: "+str(right)
    res=res+"\nПроцент правильных ответов: "+str(percent)
    res=res+"\nРезультат тестирования: "+itog
    res=res+"\nВремя: "+asctime(localtime())+"\n"

    f.write(res)
    f.close()




show_start()

root.mainloop()
