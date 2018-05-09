from tkinter import *
root = Tk()

def printName(event):
    print("Hello My Name is VSP")

button_1 = Button(root,text="Print My Name")
button_1.bind("<Button-1>",printName)
button_1.pack()

root.mainloop()