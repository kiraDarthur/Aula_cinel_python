from tkinter import *
from tkinter import messagebox


def verificar():
    login = elogin.get()
    senha = esenha.get()

    # Se estiver vazio
    if login == "" or senha == "":
        messagebox.showerror("Erro", "Preencha login e senha!")

    else:
        messagebox.showinfo("Sucesso", "Login efetuado!")


# ===================== JANELA =====================
jan = Tk()
jan.title("Login")

frame = Frame(jan)
frame.pack(padx=10, pady=10)

Label(frame, text="Login:").grid(row=0, column=0)
Label(frame, text="Senha:").grid(row=1, column=0)

elogin = Entry(frame)
esenha = Entry(frame, show="⚠")

elogin.grid(row=0, column=1)
esenha.grid(row=1, column=1)

Button(frame, text="OK", command=verificar).grid(row=2, column=0, columnspan=2)

jan.mainloop()