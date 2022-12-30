from tkinter import *
root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack(fill=y, side=RIGHT)
listbox = Listbox(root, yscrollcommand=scrollbar.set)
for i in range(200):
    listbox.insert(END, f"Item{i}")
listbox.pack(fill="both")
scrollbar.config(command=listbox.view)
root.mainloop()