from tkinter import *

root = Tk()
one = Label(root,text="One",bg="red",fg="White")
one.pack()
two = Label(root,text="One",bg="green",fg="black")
two.pack(fill=X)

three = Label(root,text="One",bg="blue",fg="black")
three.pack(side=LEFT,fill=Y)
root.mainloop()
