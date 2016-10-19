from Tkinter import *
import Image,ImageTk

root=Tk()

c=Canvas(root,width=400,height=400,bg='#005500')
c.pack()
filename='pacman.gif'
'''
c.create_image(100,100,image=ImageTk(Image.open(filename)))

cell=c.create_rectangle(40,40,60,60,outline='#ffffff')
c.configure(cell,image=PhotoImage(filename))
'''

img = PhotoImage(file="pacman.gif")
view = Label(root, image=img)
view.pack()

c.create_image(100,100,image=PhotoImage(file="pacman.gif"))

root.mainloop()
