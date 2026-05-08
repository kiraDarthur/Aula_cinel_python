from tkinter import *
from tkinter.ttk import Combobox
from tkinter.messagebox import showerror

def remover():
    nome = combo.get()
    if nome == "":
        showerror("Error","Tem que selecionar primeiro uma cidade")
    else:
        cidades.remove(nome)
        combo.configure(value=cidades)


cidades = sorted(["Porto","Lisboa","Maia"])

jan = Tk()
jan.title("Exercicio 6")
jan.geometry("300x300")
jan.iconbitmap("icon_cinel.ico")

combo = Combobox(jan, values=cidades, state="readonly")
combo.pack()
botao = Button(jan, text="Remover", command=remover)
botao.pack()


jan.mainloop()