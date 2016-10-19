#coding=utf-8
from Tkinter import *;

root=Tk()
root.title('Torrent Search')
root.geometry('800x600')
root.resizable(0,0)

Label(text='Искать: ',font='Arial 14').place(x=10,y=10)
pole=Entry(root,text='',width=57,font='Arial 14')
pole.place(x=90,y=10)
start=Button(root,text='Ok',font='Arial 12')
start.place(x=750,y=10)
text=Text(root,font='Arial 12')
text.place(x=10,y=50)





root.mainloop()
