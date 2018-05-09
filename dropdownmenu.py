from tkinter import *
import os
import platform

def donothing():
    print("Ok OK I Won't....")

    os.system ( 'date' )


root = Tk()

menu = Menu(root)
root.config(menu=menu)

submenu = Menu(menu)

menu.add_cascade(label="File",menu=submenu)
submenu.add_command(label="New Project...",command=donothing)
submenu.add_command(label="New...",command=donothing)
submenu.add_separator()
submenu.add_command(label="Exit",command=quit)

editmenu = Menu(menu)
menu.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="redo",command=donothing)


# THE TOOLBAR ***************

toolbar = Frame(root,bg="blue")
insertButt = Button(toolbar,text="insert image",command=donothing)

insertButt.pack(side=LEFT,padx=2,pady=2)
printButt = Button(toolbar,text="Print",command=donothing)
printButt.pack(side=LEFT,padx=2,pady=2)

toolbar.pack(side=TOP,fill=X)



# STATUS BAR AT THE BOTTOM


status = Label(root,text="Preparing To do Nothing...",bd=1,relief=SUNKEN,anchor=W)
status.pack(side=BOTTOM,fill=X)



root.mainloop()