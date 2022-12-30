# IMPORTAÇÃO DA BIBLIOTECA TKINTER
from tkinter import *
from tkinter import messagebox as MessageBox

# FUNÇÃO DO BOTÃO
def mensagem():
    # titulo, mensagem
    MessageBox.showinfo("Titulo da Tela", "Olá Mundo")
    
# CRIAÇÃO DA RAIZ
raiz = Tk()
# titulo
raiz.title("Titulo da tela raiz")
# dimensao da janela
raiz.geometry("250x100")
# agregando o botão
btn = Button(raiz, bg="#809A6F", fg="white", text="Da click", command=mensagem)
# colocar botão na janela
btn.place(x=30, y=25)

# rodar aplicação
raiz.mainloop()