from tkinter import *
root=Tk()

topframe = Frame(root)
topframe1 = Frame(root)
topframe.pack()
topframe1.pack()
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)


button1 = Button(topframe,text="Button 1 Man Click Me!",fg="red")
button2 = Button(topframe,text="Button 2 Man Click Me!",fg="blue")
button3 = Button(topframe,text="Button 3 Man Click Me!",bg="cyan",fg="green")
button4 = Button(bottomframe,text="Button 4 Man Click Me!",bg="black",fg="purple")

button1.pack(side=LEFT,fill=X)
button2.pack(side=LEFT,fill=Y)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)








root.mainloop()