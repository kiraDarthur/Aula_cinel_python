from tkinter import *

jan = Tk()

lfcores = LabelFrame(jan, text="Escolha uma cor: ")
lfcores.pack(side = "left")

cores = IntVar()
r1 = Radiobutton(lfcores, text="Azul", value=1,variable=cores)
r2 = Radiobutton(lfcores, text="Branco",value=2,variable=cores)
r3 = Radiobutton(lfcores, text="Amarelo",value=3,variable=cores)
r4 = Radiobutton(lfcores, text="Vermelho",value=4,variable=cores)


r1.pack(anchor=W)
r2.pack(anchor=W)
r3.pack(anchor=W)
r4.pack(anchor=W)


lfpaises = LabelFrame(jan, text="Qual o seu país de origem? ")
lfpaises.pack(side="left")

paises = IntVar()
r5 = Radiobutton(lfpaises, text="Portugal", value=1,variable=paises)
r6 = Radiobutton(lfpaises, text="Brasil", value=2,variable=paises)
r7 = Radiobutton(lfpaises, text="Angola", value=3,variable=paises)

r5.pack(anchor=W)
r6.pack(anchor=W)
r7.pack(anchor=W)

jan.mainloop()