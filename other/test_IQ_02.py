# coding: utf-8
# Шокин Евгений. задание Проектирование GUI. Программа тестирования.
# ещё нужно сделать: 1. сделать неактивными кнопки с клавы Enter S R и Q когда они не отображаются
# 		     2. + проблема с именами набранными кириллицей
#		     3. + обрезание текста снизу в Label-ах
#		     4. + запрет на продолжить если поле ввода пустое или не сделан выбор
# 		     5. +- цвет текста в лэйблах, а так же выравнивание по гориз и верт
#		     6. добавить прогрессбар (четыре прямоугольничка с номерами вопросов)
#		     7. + добавить подсказки в заданиях
# 		     8. + обнулить радиобатн и чекбоксы при повторном тесте
# 		     9. + почему-то офис не равно офис
#                    10. + добавить время тестирования
import tkMessageBox
from Tkinter import *
from time import localtime,asctime
import time

root = Tk() # главное окно
root.title("Test_ment") # заголовок окна
root.geometry('800x480+600+400')
root.resizable(False, False)
root["bg"] = "#eeeeee"

ball,page,num=0,0,0
name,word='',''
ocenka=''
test_time=0
#
#
def next_page(event=1):
    global ball,page,name,user_name,num,word,test_time
    page=page+1
    if page==1 and user_name.get()=='':
        page=0
        tkMessageBox.showwarning("Ошибка","Вы забыли ввести Ваше имя")
    elif page==1:
        test_time=time.clock() # старт тестирования
        name=user_name.get()
        user_name.set('')
        text_voprosa.configure(text='Введите следующее число:')
        text_podskazka.configure(text='продолжите ряд чисел')
        page1_fibon.place(x=25, y=220, width=325, height=30)
    elif page==2 and user_name.get()=='':
        page=1
        tkMessageBox.showwarning("Ошибка","Введите число")
    elif page==2:
        if user_name.get().isdigit():
            num=int(user_name.get())
            if num==5:
                ball=ball+1             # ball
            user_name.set('')
        else:
            page=1
            user_name.set('')
            tkMessageBox.showwarning("Ошибка","Введите число")
            return
        text_voprosa.configure(text='Впишите лишнее слово:')
        text_podskazka.configure(text='одно слово без пробелов из списка')
        #text_result.configure(text=ball) # remove
        page1_fibon.place_forget()
        page2_homes.place(x=125, y=210, width=165, height=200)
    elif page==3:
        if user_name.get().isalpha():
            word=user_name.get()
            if word.encode('utf8')=='офис':
                ball=ball+1             # ball
            user_name.set('')
        else:
            page=2
            user_name.set('')
            tkMessageBox.showwarning("Ошибка","Введите слово")
            return
        text_voprosa.configure(text='Отметьте лишнее слово:')
        text_podskazka.configure(text='выберите одно слово из списка')
        text_podskazka.place(x=160, y=185, width=500, height=15)
        #text_result.configure(text=ball) # remove
        page2_homes.place_forget()
        ent.place_forget()
        rad0.place(x=165, y=220, width=155, height=30)
        rad1.place(x=165, y=250, width=155, height=30)
        rad2.place(x=165, y=280, width=155, height=30)
        rad3.place(x=165, y=310, width=155, height=30)
        rad4.place(x=165, y=340, width=155, height=30)
    elif page==4:
        rad_btn=var.get()
        if rad_btn==1:
            ball=ball+1             # ball
        var.set(0)
        text_voprosa.configure(text='Найдите сочетания, не образующие марку авто:')
        text_voprosa.place(x=15, y=155, width=580, height=30)
        text_podskazka.configure(text='выберите несколько вариантов')
        text_podskazka.place(x=160, y=185, width=500, height=15)
        #text_result.configure(text=ball) # remove
        rad0.place_forget()
        rad1.place_forget()
        rad2.place_forget()
        rad3.place_forget()
        rad4.place_forget()
        che1.place(x=215, y=220, width=155, height=30)
        che2.place(x=215, y=250, width=155, height=30)
        che3.place(x=215, y=280, width=155, height=30)
        che4.place(x=215, y=310, width=155, height=30)
        che5.place(x=215, y=340, width=155, height=30)
        che6.place(x=215, y=370, width=155, height=30)
    elif page==5:
        if var3.get()==1 and var6.get()==1:
            ball=ball+1             # ball
        var1.set(0)
        var2.set(0)
        var3.set(0)
        var4.set(0)
        var5.set(0)
        var6.set(0)
        raschet_ocenki()
        text_zagolovok.configure(text='Результаты теста №1:')
        text_result.configure(text='Имя тестируемого: '+name.encode('utf8')+'\nВы набрали '+str(ball)+' баллов\nМаксимум баллов 4\nВаша оценка - '+ocenka+'\nВы отвечали на тест '+str(test_time)+' секунд',fg='#666666',font="Arial 18")
        text_result.place(x=10, y=120, width=600, height=300)
        text_voprosa.place_forget()
        text_podskazka.place_forget()
        che1.place_forget()
        che2.place_forget()
        che3.place_forget()
        che4.place_forget()
        che5.place_forget()
        che6.place_forget()
        btn_next.place_forget()
        btn_snova.place(x=615, y=270, width=155, height=30)
        btn_save.place(x=615, y=315, width=155, height=30)
        btn_quit.place(x=615, y=360, width=155, height=30)
    else:
        page=0
        ball=0
        text_zagolovok.configure(text='Тест на сообразительность №1')
        text_voprosa.configure(text='Введите Ваше имя:')
        text_voprosa.place(x=25, y=155, width=330, height=30)
        text_podskazka.configure(text='ник, прозвище, поганяло, ID, порядковый номер')
        btn_next.place(x=615, y=155, width=155, height=30)
        ent.place(x=415, y=155, width=155, height=30)
        text_podskazka.place(x=220, y=185, width=500, height=15)
        text_voprosa.place(x=25, y=155, width=330, height=30)
        text_result.place_forget()
        btn_snova.place_forget()
        btn_save.place_forget()
        btn_quit.place_forget()

def raschet_ocenki():
    global ocenka,ball,test_time
    if ball==4:
        ocenka='Отлично'
    elif ball==3:
        ocenka='Хорошо'
    elif ball==2:
        ocenka='Удовлетворительно'
    elif ball==1:
        ocenka='Неудовлетворительно'
    else:
        ocenka='Очччень плохо!'
    # расчет секунд
    test_time=int(time.clock()-test_time)
    

def save_results(event=1):
    global name, ocenka, ball, test_time
    f=open('test_result.txt','a+')
    r='-----  Тест на сообразительность №1  -----'
    r=r+'\nВремя и дата: '+asctime(localtime())
    r=r+'\nИмя тестируемого: '+name.encode('utf8')
    r=r+'\nКоличество набранных баллов: '+str(ball)
    r=r+'\nМаксимально возможное количество баллов: 4'
    r=r+'\nОценка тестирования: '+ocenka
    r=r+'\nВремя, потраченное на тест: '+str(test_time)+' секунд'
    r=r+'\n'
    

    f.write(r)
    f.close()

    tkMessageBox.showwarning("Сохранение результата","Результат сохранен в файл test_result.txt")
        
def close_win(event=1):
     root.destroy()
# ----------------------------------------------------------
def output():
    global ball,page
    s=ent.get()
    if s == '1':
        ball=ball+1
        
def funk1():
    text_voprosa.configure(text='Нажата кнопка выход')
    
def funk(event=1):
    return
# -----------------------------------------------------------

# Фреймы
#fra1 = Frame(root,width=500,height=100,bg="darkred")
#fra1.pack()
# Поле ввода
user_name=StringVar()
ent = Entry(root,width=1,takefocus=TRUE,textvariable=user_name)
ent.place(x=415, y=155, width=155, height=30)
# Дочерние окна
#nullEntry = Toplevel(root,bd=10,bg="#eeeeee")
#nullEntry.geometry('300x80+860+540')
#nullEntry.resizable(False, False)
# Радиобулки
var=IntVar()
var.set(0)
rad0 = Radiobutton(root,text='селёдка',variable=var,value=0,font="Arial 18")
rad1 = Radiobutton(root,text='кит',variable=var,value=1,font="Arial 18")
rad2 = Radiobutton(root,text='акула',variable=var,value=2,font="Arial 18")
rad3 = Radiobutton(root,text='барракуда',variable=var,value=3,font="Arial 18")
rad4 = Radiobutton(root,text='треска',variable=var,value=4,font="Arial 18")
#rad0.place(x=215, y=220, width=155, height=30)
#rad1.place(x=215, y=250, width=155, height=30)
#rad2.place(x=215, y=280, width=155, height=30)
#rad3.place(x=215, y=310, width=155, height=30)
#rad4.place(x=215, y=340, width=155, height=30)
# Полоски-разделители пространства
c = Canvas(root, width=300, height=300, bg="white")
c.create_rectangle((105, 105, 150, 130), fill="red",outline="grey", width="1")
# Чурекбоксы
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
che1 = Checkbutton(root,text="рофд",variable=var1,onvalue=1,offvalue=0,font="Arial 14")
che2 = Checkbutton(root,text="таиф",variable=var2,onvalue=1,offvalue=0,font="Arial 14")
che3 = Checkbutton(root,text="сатнарат",variable=var3,onvalue=1,offvalue=0,font="Arial 14")
che4 = Checkbutton(root,text="тбнеил",variable=var4,onvalue=1,offvalue=0,font="Arial 14")
che5 = Checkbutton(root,text="ожеп",variable=var5,onvalue=1,offvalue=0,font="Arial 14")
che6 = Checkbutton(root,text="гбион",variable=var6,onvalue=1,offvalue=0,font="Arial 14")
#che1.place(x=215, y=220, width=155, height=30)
#che2.place(x=215, y=250, width=155, height=30)
#che3.place(x=215, y=280, width=155, height=30)
#che4.place(x=215, y=310, width=155, height=30)
#che5.place(x=215, y=340, width=155, height=30)
#che6.place(x=215, y=370, width=155, height=30)

# Текстовые лэйблы
text_zagolovok=Label(root,text='Тест на сообразительность №1',fg='#eeeeee',bg='#cccccc',font=('Arial', 30, 'bold'))
text_voprosa=Label(root,text='Введите Ваше имя:',font="Arial 18") # question
text_podskazka=Label(root,text='ник, прозвище, поганяло, ID, порядковый номер')
page1_fibon=Label(root,text='0  1  1  2  3  _',font="Arial 24")
page2_homes=Label(root,text='дом\nиглу\nбунгало\nофис\nхижина',font="Arial 24")
text_footer=Label(root,text='ООО "Тестирование мозгов"',bg='#cccccc')
#text_forgotName=Label(nullEntry,text='Вас что, в детстве ни как не назвали?')
text_result=Label(root,text=ball)
text_zagolovok.place(x=0, y=0, width=800, height=120)
text_voprosa.place(x=25, y=155, width=330, height=30)
text_podskazka.place(x=220, y=185, width=500, height=15)
#page1_fibon.place(x=25, y=220, width=325, height=30)
#page2_homes.place(x=125, y=210, width=165, height=200)
text_footer.place(x=0, y=440, width=800, height=40)
#text_forgotName.place(x=0, y=0, width=290, height=15)
#text_result.place(x=0, y=410, width=400, height=40)

# Кнопки
btn_next=Button(root, text='Продолжить (Enter)',bg='#cccccc',command=next_page)
#btn_escho=Button(nullEntry, text='Попробую вспомнить!',bg='#cccccc',command=funk)
btn_snova=Button(root, text='Попробовать снова (R)',bg='#cccccc',command=next_page)
btn_save=Button(root, text='Сохранить результат (S)',bg='#cccccc',command=save_results)
btn_quit=Button(root, text='Выход (Esc)',bg='#cccccc',command=close_win)

# Кнопки на клаве
root.bind("<KeyPress-Return>",next_page)
root.bind("<KeyPress-r>",next_page)
root.bind("<KeyPress-s>",save_results)
root.bind("<KeyPress-Escape>",close_win)

# Расположение кнопок

#btn_snova.place(x=615, y=270, width=155, height=30)
#btn_save.place(x=615, y=315, width=155, height=30)
#btn_quit.place(x=615, y=360, width=155, height=30)
btn_next.place(x=615, y=155, width=155, height=30)
#btn_escho.place(x=70, y=25, width=150, height=30)

root.mainloop()
