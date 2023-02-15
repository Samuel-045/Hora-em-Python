from tkinter import * #importa o tkinter
from tkinter.ttk import *
from time import strftime #importa o relógio

root = Tk() #janela
root.title('Horário real') #título da janela


def time():
    string = strftime('%H:%M:%S %p') #configuração da exibição
    lbl.config(text=string)
    lbl.after(1000, time)


lbl = Label(root, font=('calibri', 40, 'bold'),
            background='black',
            foreground='white')
lbl.pack(anchor='center')
time()

mainloop()