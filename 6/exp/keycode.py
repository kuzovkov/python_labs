#coding=utf-8
import Tkinter


root = Tkinter.Tk()
root.title("Регистратор символов клавиатуры")

def reportEvent(event):
        print 'keysym=%s, keysym_num=%s' % (event.keysym, event.keysym_num)
        label['text']=event.keysym +" ==> " + str(event.keysym_num)

text  = Tkinter.Text(root, width=20, height=3, highlightthickness=2,font='Arial 20')


text.bind('<KeyPress>', reportEvent)

text.pack(expand=1, fill="both")
text.focus_set()

label=Tkinter.Label(root,width=20,height=3,font='Arial 20')
label.pack()
root.mainloop()

