from tkinter import *
import os
import platform
import pexpect
import sys
def donothing():
    os.system('sudo ansible all -a \'/bin/mkdir /root/Desktop/'+e1.get()+'\'');
    print("Ok OK I Won't....")
    x = str(input("Enter"))
    y = 'su',x
    s = ''
    for i in y:
        s += i+' '

    print(s)



    proc = pexpect.spawn(s)
    proc.expect("Password")
    proc.sendline("redhat")
    proc.expect("$")
    proc.sendline("whoami")

    proc.expect("$")
    proc.sendline("ls -al")
    proc.expect("$")







root = Tk()





menu = Menu(root)
root.config(menu=menu)

two = Label(root,text="Welcome To Network Remote",bg="green",fg="black")

entryText = Label(root,text="Enter Directory Name",bg="green",fg="black")
two.pack(fill=X)
entryText.pack(fill=X);

e1 = Entry(root);
e1.pack(fill=X);



submenu = Menu(menu)

menu.add_cascade(label="Controls",menu=submenu)
submenu.add_command(label="File Control",command=donothing)
submenu.add_command(label="Installation Control",command=donothing)
submenu.add_command(label="",command=donothing)

submenu.add_separator()
submenu.add_command(label="Exit",command=quit)

editmenu = Menu(menu)
menu.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="redo",command=donothing)


# THE TOOLBAR ***************

toolbar = Frame(root,bg="blue")
insertButt = Button(toolbar,text="Make Directory",command=donothing)

insertButt.pack(side=LEFT,padx=2,pady=2)
printButt = Button(toolbar,text="Print",command=donothing)
printButt.pack(side=LEFT,padx=2,pady=2)

toolbar.pack(side=TOP,fill=X)



# STATUS BAR AT THE BOTTOM


status = Label(root,text="Preparing To do Nothing...",bd=1,relief=SUNKEN,anchor=W)
status.pack(side=BOTTOM,fill=X)



root.mainloop()