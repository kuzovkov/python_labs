from Tkinter import *
import time
i = 0
def tick():
    global i
    i+= 1
    if i > 1000: i = 0
    label['text'] = i
    label.after(200, tick)
    
root=Tk()
label = Label(font='sans 20')
label.pack()
label.after_idle(tick)
root.mainloop()
