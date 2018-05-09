from tkinter import *
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo("Window Title ... Monkeys can live up to 300 years ")

answer = tkinter.messagebox.askquestion("Question 1--Do You Love China?")

if answer == 'yes':
    print("Thats My Girl Asshole! Back off!")


Label(root,text="Enter Directory Name").grid(row=10);
e1 = Entry(root)
e1.grid(row=11,column=1);


root.mainloop()