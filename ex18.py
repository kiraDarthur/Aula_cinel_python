#Desenvolva uma pequena interface, usando raduobutton, para escolher o genero de uma pessoa.
def ler():
    opçao = genero.get()
    showinfo("opçao escolhida...", "o valor" 
             f" associado ao botão Radio é «{genero.get()}»")

from tkinter import *
from tkinter.messagebox import  showinfo

jan = Tk()

jan.title("Exercício 3")
jan.geometry("300x200")
jan.iconbitmap("icon_cinel.ico")

lfgenero = LabelFrame(jan, text="Escolha o género...")
lfgenero.pack(expand=True,fill=BOTH)#fill preenche na largura do eixo X

##LabelFrame
genero = StringVar(value="Feminino")

rMasc = Radiobutton(lfgenero, text="Masculino",
                    value="Masculino",variable=genero, command=ler)
rFem = Radiobutton(lfgenero, text="Feminino",
                   value="Feminino",variable=genero, command=ler)
rOutro = Radiobutton(lfgenero, text="NS/NR",
                     value="NS/NR",variable=genero, command=ler)

rFem.grid(row=0, column=0,stick=W)
rMasc.grid(row=1, column=0,stick=W)
rOutro.grid(row=3, column=0,stick=W)

jan.mainloop()
