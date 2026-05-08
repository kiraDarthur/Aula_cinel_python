from tkinter import *

jan = Tk()

jan.geometry("300x300")

luser = Label(jan, text="Username:").grid(row=0, column=0)
lpass = Label(jan, text="Password:").grid(row=1, column=0)
euser = Entry(jan, width=30, bg="grey80",   relief="rifge")
euser = Entry(jan, width=30, bg="grey80", relief="ridge").grid(row=0, column=1)
epass = Entry(jan, width=30, bg="grey80", relief="ridge",show="*").grid(row=1, column=1)