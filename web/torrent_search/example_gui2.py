#coding=utf-8
from Tkinter import *
import tkFileDialog
import webbrowser
from ScrolledText import ScrolledText

cnt=0
res_ls=[
['tfile.me','Антивирус Касперсткого Скачать Бесплатно Антивирус Касперсткого Скачать Бесплатно Антивирус Касперсткого Скачать Бесплатно','35 MB','2013-10-23 13:34','http://www.yandex.ru','No Proxy','#ff33bb'],
['tfile.me','Windows 8 Скачать Бесплатно Тря ля ля','3500 MB','2013-10-23 13:34','http://www.rambler.ru','No Proxy','#ff33bb'],
['tfile.me','Антивирус Доктов ВЕБ Сачать Бесплатно Антивирус Доктов ВЕБ Сачать Бесплатно Антивирус Доктов ВЕБ Сачать Бесплатно','45 MB','2013-10-23 13:34','http://mail.ru','182.62.12.45:8080','#ff33bb'],
['tfile.me','Антивирус Avira Сачать Бесплатно Антивирус Avira Сачать Бесплатно Антивирус Avira Сачать Бесплатно','100 MB','2013-10-23 13:34','http://ya.ru','236.23.45.12:8888','#ff33bb'],
['tfile.me','Антивирус Касперсткого Скачать Бесплатно Антивирус Касперсткого Скачать Бесплатно Антивирус Касперсткого Скачать Бесплатно','35 MB','2013-10-23 13:34','http://www.yandex.ru','No Proxy','#ff33bb'],
['tfile.me','Windows 8 Скачать Бесплатно Тря ля ля','3500 MB','2013-10-23 13:34','http://www.rambler.ru','No Proxy','#ff33bb'],
['tfile.me','Антивирус Доктов ВЕБ Сачать Бесплатно Антивирус Доктов ВЕБ Сачать Бесплатно Антивирус Доктов ВЕБ Сачать Бесплатно','45 MB','2013-10-23 13:34','http://mail.ru','182.62.12.45:8080','#ff33bb'],
['tfile.me','Антивирус Avira Сачать Бесплатно Антивирус Avira Сачать Бесплатно Антивирус Avira Сачать Бесплатно','100 MB','2013-10-23 13:34','http://ya.ru','236.23.45.12:8888','#ff33bb'],
['tfile.me','Антивирус Касперсткого Скачать Бесплатно Антивирус Касперсткого Скачать Бесплатно Антивирус Касперсткого Скачать Бесплатно','35 MB','2013-10-23 13:34','http://www.yandex.ru','No Proxy','#ff33bb'],
['tfile.me','Windows 8 Скачать Бесплатно Тря ля ля','3500 MB','2013-10-23 13:34','http://www.rambler.ru','No Proxy','#ff33bb'],
['tfile.me','Антивирус Доктов ВЕБ Сачать Бесплатно Антивирус Доктов ВЕБ Сачать Бесплатно Антивирус Доктов ВЕБ Сачать Бесплатно','45 MB','2013-10-23 13:34','http://mail.ru','182.62.12.45:8080','#ff33bb'],
['tfile.me','Антивирус Avira Сачать Бесплатно Антивирус Avira Сачать Бесплатно Антивирус Avira Сачать Бесплатно','100 MB','2013-10-23 13:34','http://ya.ru','236.23.45.12:8888','#ff33bb'],
['tfile.me','Антивирус Касперсткого Скачать Бесплатно Антивирус Касперсткого Скачать Бесплатно Антивирус Касперсткого Скачать Бесплатно','35 MB','2013-10-23 13:34','http://www.yandex.ru','No Proxy','#ff33bb'],
['tfile.me','Windows 8 Скачать Бесплатно Тря ля ля','3500 MB','2013-10-23 13:34','http://www.rambler.ru','No Proxy','#ff33bb'],
['tfile.me','Антивирус Доктов ВЕБ Сачать Бесплатно Антивирус Доктов ВЕБ Сачать Бесплатно Антивирус Доктов ВЕБ Сачать Бесплатно','45 MB','2013-10-23 13:34','http://mail.ru','182.62.12.45:8080','#ff33bb'],
['tfile.me','Антивирус Avira Сачать Бесплатно Антивирус Avira Сачать Бесплатно Антивирус Avira Сачать Бесплатно','100 MB','2013-10-23 13:34','http://ya.ru','236.23.45.12:8888','#ff33bb'],
['tfile.me','Антивирус Касперсткого Скачать Бесплатно Антивирус Касперсткого Скачать Бесплатно Антивирус Касперсткого Скачать Бесплатно','35 MB','2013-10-23 13:34','http://www.yandex.ru','No Proxy','#ff33bb'],
['tfile.me','Windows 8 Скачать Бесплатно Тря ля ля','3500 MB','2013-10-23 13:34','http://www.rambler.ru','No Proxy','#ff33bb'],
['tfile.me','Антивирус Доктов ВЕБ Сачать Бесплатно Антивирус Доктов ВЕБ Сачать Бесплатно Антивирус Доктов ВЕБ Сачать Бесплатно','45 MB','2013-10-23 13:34','http://mail.ru','182.62.12.45:8080','#ff33bb'],
['tfile.me','Антивирус Avira Сачать Бесплатно Антивирус Avira Сачать Бесплатно Антивирус Avira Сачать Бесплатно','100 MB','2013-10-23 13:34','http://ya.ru','236.23.45.12:8888','#ff33bb'],
['tfile.me','Антивирус Касперсткого Скачать Бесплатно Антивирус Касперсткого Скачать Бесплатно Антивирус Касперсткого Скачать Бесплатно','35 MB','2013-10-23 13:34','http://www.yandex.ru','No Proxy','#ff33bb'],
['tfile.me','Windows 8 Скачать Бесплатно Тря ля ля','3500 MB','2013-10-23 13:34','http://www.rambler.ru','No Proxy','#ff33bb'],
['tfile.me','Антивирус Доктов ВЕБ Сачать Бесплатно Антивирус Доктов ВЕБ Сачать Бесплатно Антивирус Доктов ВЕБ Сачать Бесплатно','45 MB','2013-10-23 13:34','http://mail.ru','182.62.12.45:8080','#ff33bb'],
['tfile.me','Антивирус Avira Сачать Бесплатно Антивирус Avira Сачать Бесплатно Антивирус Avira Сачать Бесплатно','100 MB','2013-10-23 13:34','http://ya.ru','236.23.45.12:8888','#ff33bb']


       ]

root = Tk()
root.title('Torrent Search')
#root.resizable(0,0)



def search(e):
    global res_ls
    global title_ls,cnt
    cnt=0
    textbox.delete(1.0,END)
    hframe=Frame(width=900,height=20)
    torrent=Button(hframe,text='Torrent', height=1,width=20,bg="#777777",justify='center', bd=2)
    torrent.pack(side='left')
    title=Button(hframe,text='Title', width=90,height=1,bg="#777777",justify='center', bd=2)
    title.pack(side='left')
    size=Button(hframe,text='Size', width=7,height=1,bg="#777777", bd=2,justify='center')
    size.pack(side='left')
    date=Button(hframe,text='Date', width=16,height=1,bg="#777777", bd=2,justify='center')
    date.pack(side='left')
    proxy=Button(hframe,text='Proxy', width=30,height=1,bg="#777777", bd=2,justify='center')
    proxy.pack(side='left')
    textbox.window_create(END,window=hframe)
    
    for item in res_ls:        
        frame=Frame(width=900,height=40)
        torrent=Button(frame,text=item[0], height=3,width=20,bg=item[6],justify='left')
        torrent.pack(side='left')
        title=Button(frame,text=item[1], width=90,height=3,wraplength=500,bg=item[6],justify='left',command=lambda x=cnt: clickItem(x))
        title.pack(side='left')
        size=Button(frame,text=item[2], width=7,height=3,bg=item[6], bd=2)
        size.pack(side='left')
        date=Button(frame,text=item[3], width=16,height=3,bg=item[6], bd=2)
        date.pack(side='left')
        proxy=Button(frame,text=item[5], width=30,height=3,bg=item[6], bd=2,justify='center')
        proxy.pack(side='left')
        textbox.window_create(END,window=frame)
        cnt+=1
    

def Quit(ev):
    root.destroy()

def clickItem(i):
    global res_ls
    print "i= ",i,"title=",res_ls[i][1].decode('utf-8')
    webbrowser.open(res_ls[i][4])

panelFrame = Frame(root, height = 60, bg = 'gray')
textFrame = Frame(root, height = 340, width = 900)

panelFrame.pack(side = 'top', fill = 'x')
textFrame.pack(side = 'bottom', fill = 'both', expand = 1)

textbox = ScrolledText(textFrame, font='Arial 14',wrap='word',width=95)
scrollbar = Scrollbar(textFrame)
scrollbarx = Scrollbar(textFrame)

scrollbar['command'] = textbox.yview
textbox['yscrollcommand'] = scrollbar.set


scrollbarx['command'] = textbox.xview
scrollbarx['orient'] = 'horizontal'
#scrollbarx['width'] = 600
textbox['xscrollcommand'] = scrollbarx.set

textbox.pack(side = 'left', fill = 'both', expand = 1)
scrollbar.pack(side = 'right', fill = 'y')

scrollbarx.pack(side = 'bottom', fill = 'x')
entry=Entry(panelFrame,width=80,font='arial 12')
entry.place(x=10,y=10)
loadBtn = Button(panelFrame, text = 'Search')
quitBtn = Button(panelFrame, text = 'Quit')


loadBtn.bind("<Button-1>",search)
quitBtn.bind("<Button-1>", Quit)


loadBtn.place(x = 800, y = 10, width = 40, height = 40)
quitBtn.place(x = 850, y = 10, width = 40, height = 40)


torrent=Button(text='Torrent', height=1,width=20,bg="#777777",justify='center', bd=2)
textbox.window_create(END,window=torrent)
title=Button(text='Title', width=90,height=1,bg="#777777",justify='center', bd=2)
textbox.window_create(END,window=title)
size=Button(text='Size', width=7,height=1,bg="#777777", bd=2,justify='center')
textbox.window_create(END,window=size)
date=Button(text='Date', width=16,height=1,bg="#777777", bd=2,justify='center')
textbox.window_create(END,window=date)
proxy=Button(text='Proxy', width=30,height=1,bg="#777777", bd=2,justify='center')
textbox.window_create(END,window=proxy)


root.mainloop()
