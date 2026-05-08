#Desenvolva uma pequena interface , usando checbutton, para escolher quais as marcas de automveis que mais gosta

from tkinter import *
jan = Tk()

def selecionar():
    m1V.set(True)
    m2V.set(True)
    m3V.set(True)
    m4V.set(True)
    m5V.set(True)

def limpar():
    m1V.set(False)
    m2V.set(False)
    m3V.set(False)
    m4V.set(False)
    m5V.set(False)


jan.title("Exercicio 4")
jan.geometry("300x200")
jan.iconbitmap("icon_cinel.ico")
lframe = LabelFrame(jan , text="Escolha marcas favoritas")
lframe.pack()

m1V = BooleanVar()
marca1 = Checkbutton(lframe, text="Fiat", variable=m1V)
m2V = BooleanVar()
marca2 = Checkbutton(lframe, text="Audi", variable=m2V)
m3V = BooleanVar()
marca3 = Checkbutton(lframe, text="VW", variable=m3V)
m4V = BooleanVar()
marca4 = Checkbutton(lframe, text="BMW", variable=m4V)
m5V = BooleanVar()
marca5 = Checkbutton(lframe, text="Seat", variable=m5V)

marca1.grid(row=0, column= 0, stick=W)
marca2.grid(row=1, column= 0, stick=W)
marca3.grid(row=2, column= 0, stick=W)
marca4.grid(row=3, column= 0, stick=W)
marca5.grid(row=4, column= 0, stick=W)

botao = Button(jan, text="Select All", command=selecionar,bg="blue")
botao.pack()
botao2 = Button(jan, text="Clear All", command=limpar,bg="red")
botao2.pack()



jan.mainloop()