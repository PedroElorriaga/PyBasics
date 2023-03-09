from tkinter import *

janela = Tk()
janela.wm_resizable(width=False, height=False)

box1 = Label(janela, text="Yellow", bg="yellow", foreground="black", width=10, height= 5)
box2 = Label(janela, text="Red", bg="red", foreground="white", width=10, height= 5)
box3 = Label(janela, text="Black", bg="black", foreground="white", width=10, height= 5)
box4 = Label(janela, text="Orange", bg="orange", foreground="white", width=10, height= 5)
box5 = Label(janela, text="Pink", bg="pink", foreground="black", width=10, height= 5)
box6 = Label(janela, text="Purple", bg="purple", foreground="white", width=10, height= 5)

box1.grid(column= 0, row= 0)
box2.grid(column= 1, row= 0)
box3.grid(column= 0, row= 1)
box4.grid(column= 1, row= 1)
box5.grid(column= 0, row= 2)
box6.grid(column= 1, row= 2)

boxvertical = Label(janela, text="Vertical", bg="white", foreground="black")
boxhorizontal = Label(janela, text="Horizontal", bg="white", foreground="black", height=2)

boxvertical.grid(column=2, row=0, rowspan=4, sticky=N+S)
boxhorizontal.grid(column=0, row=3, columnspan=3, sticky=W+E)

janela.mainloop()