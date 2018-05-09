from tkinter import *


class BuckyButtons:

    def __init__(self,master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame,text="Print_Message",command=self.printMessage)

        self.printButton.pack(side=LEFT)

        self.QuitButton = Button(frame,text="Quit",command=frame.quit)

        self.QuitButton.pack(side=LEFT)


    def printMessage(self):
        print("WOOW THIS ACTUALLY WORKED!")








root = Tk()

b = BuckyButtons(root)






root.mainloop()