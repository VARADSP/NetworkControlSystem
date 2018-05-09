import tkinter as tk
from PIL import ImageTk

root = tk.Tk()
def make_button():
    b = tk.Button(root)
    image = ImageTk.PhotoImage(file="896 (5).jpg")
    b.config(image = image)
    b.image=image

    b.pack()

make_button()
root.mainloop()