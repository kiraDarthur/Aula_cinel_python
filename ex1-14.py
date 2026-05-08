from tkinter import *

jan = Tk()

#2
jan.title("Primeira janela em TK")

#3)alterar o fundo da janela para  Laranja
jan["bg"] = "red"

#4)Defina as dimensões da janela para 400 x 330 pixéis
jan.geometry("400x330")

#5)Não permita que a janela seja redimensionada quer na largura, quer na altura.
jan.resizable(0,0)

#6)Defina uma variável “fonte” para as caraterísticas "Comic Sans MS", tamanho 14
#e negrito. (Sugestão: Crie um tuplo com estes dados).

fonte = ("Comic Sans MS", 14, "bold")

#7)
jan.iconbitmap("icon_cinel.ico")

#8)

jan.geometry("400x330+300+500")

#9)

ltexto = Label(jan, text="Olá Python")
ltexto.pack()

#10)

#ltexto["font"] = fonte
ltexto.configure(font=fonte, fg ="blue")

#11)

expto = Entry(jan, width=5,bg="salmon",relief="ridge",
              fg="brown", font=("Algerinan",13))

expto.pack()

#12)

bsair = Button(jan, text="Sair", font=fonte, bd=7)
bsair.pack()

#13)

bsair.configure(command=lambda:jan.destroy())

#14)
bsair.configure(bd=3, bg="#1A095C", fg="#DDBBAA")
bsair.configure(highlightbackground="orange",
                highlightcolor="white")


jan.mainloop()