from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x200")
messagebox.askretrycancel("Application", "Tentar novamente?")

root.mainloop()