from Tkinter import *
from PIL import Image, ImageTk

root = Tk()
'''
img = PhotoImage(file="04.gif",width=400,height=400)
view = Label(root, image=img)
view.pack()
'''
 
image = Image.open("img/04.gif") 
photo = ImageTk.PhotoImage(image)
label = Label(root) 

label.pack()
label.configure(image=photo)
mainloop()
