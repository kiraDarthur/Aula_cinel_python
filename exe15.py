from tkinter import *
from posicao import *

# ===================== JANELA =====================
jan = Tk()
jan.title("Nova Janela")
jan.resizable(0, 0)

jan.geometry("350x350")  # simplifiquei
#jan.configure(bg="#0f172a")
jan.iconbitmap("icon_cinel.ico")

# ===================== FRAMES =====================

# Criar frames SEPARADAMENTE
f1 = Frame(jan)
f2 = Frame(jan)
f3 = Frame(jan)

# Posicionar frames
f1.pack(pady=10)
f2.pack(pady=10)
f3.pack(pady=10)

# ===================== CAMPOS =====================

lnome = Label(f1, text="Name:")
lmorada = Label(f1, text="Morada:")

enome = Entry(f1)
emorada = Entry(f1)

lnome.grid(row=0, column=0)
lmorada.grid(row=1, column=0)
enome.grid(row=0, column=1)
emorada.grid(row=1, column=1)

# ===================== FUNÇÕES =====================

def ler():
    nome = enome.get()
    morada = emorada.get()

    ltxtnome["text"] = "Nome: " + nome
    ltxtmorada["text"] = "Morada: " + morada

def pegar():
    nome = enome.get()
    morada = emorada.get()
    ltxtnome["text"] = nome
    ltxtmorada.configure(text=morada, font=("Arial",11,"underline"))
def limpar():
    enome.delete(0, END)
    emorada.delete(0, END)
    enome.focus()
    ltxtnome["text"] = ""
    ltxtmorada["text"] = ""

def sair():
    jan.destroy()

# ===================== BOTÕES =====================

bluer = Button(f2, text="Ler Dados", width=10, bd=4, command=ler)
blimpar = Button(f2, text="Limpar", width=10, bd=4, command=limpar)
bsair = Button(f2, text="Sair", bd=4, bg="red", command=sair)

bluer.pack(side="left", padx=5)
blimpar.pack(side="left", padx=5)
bsair.pack(side="left", padx=5)

# ===================== RESULTADO =====================

ltexto = Label(f3, text="Os dados lidos são:")
ltxtnome = Label(f3)
ltxtmorada = Label(f3)

ltexto.pack(pady=5)
ltxtnome.pack(pady=5)
ltxtmorada.pack(pady=5)

# ===================== LOOP =====================
jan.mainloop()