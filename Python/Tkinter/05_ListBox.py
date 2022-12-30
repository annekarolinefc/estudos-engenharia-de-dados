from tkinter import *

root = Tk()
root.geometry("200x200")

frame = Frame(root)
frame.pack()

label = Label(root, text="Lista de items de um Supermercado")
label.pack()

listbox = Listbox(root)

listbox.insert(1, "Pão")
listbox.insert(2, "Leite")
listbox.insert(3, "Carne")
listbox.insert(4, "Queijo")
listbox.insert(5, "Vegetais")

listbox.pack()

root.mainloop()