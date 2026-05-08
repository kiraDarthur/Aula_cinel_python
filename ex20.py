from tkinter import *
from  tkinter.ttk import Combobox
listaAlunos = ("Ana","João","Maria","Marta")


jan = Tk()
jan.title("Exercio 5")
jan.geometry("300x300")
jan.iconbitmap("icon_cinel.ico")

combo = Combobox(jan, values=listaAlunos, state="readonly")
combo.pack()

jan.mainloop()