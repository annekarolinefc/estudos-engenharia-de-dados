from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x200")

def hello():
    messagebox.showinfo("Diga Olá!", "Olá mundo")
    
a = Button(root, text="Diga olá", command=hello)
a.pack()

root.mainloop()