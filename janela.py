##BIGS
from tkinter import *
from posicao import centrar

#VARS
font1 = ("Arial", 14, "bold")
font2 = ("Comic Sans MS", 14)

##DEFS
def bazar():
    jan.destroy()

#########################GUI
larg,alt = 500,200
jan =  Tk()
jan.title("<<< A minha primeira janela!! >>>")
jan.iconbitmap("icon_cinel.ico")
jan.geometry(centrar(jan,larg,alt))


jan.resizable(0,1)
#jan.state("iconic") #jan.state("zoomed")

lnome = Label(jan, text="Nome:", font=font1)
lidade = Label(jan, text="Idade:", font=font1)
lnome.grid(row=0, column= 0)
lidade.grid(row=1, column= 0)


enome = Entry(jan,bg="grey", font=font2)
eidade = Entry(jan,bg="grey", font=font2)
enome.grid(row=0, column= 1)
eidade.grid(row=1, column= 1)



bsair = Button(jan, text="Sair", width=6, font= font1,
               bg="red", fg="white",command=bazar)

bler = Button(jan,text="Ler\nDados",bd=4,font=font1)

bsair.grid(row=2, column= 2)
bler.grid(row=2, column= 1)
#bsair.place(x=250,y=100)


jan.mainloop()