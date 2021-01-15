#aus
#https://ichlernepython.blogspot.com/2018/02/grid-einen-taschenrechner-programmieren.html


from tkinter import *
from math import *

top = Tk()

top.title("Taschenrechner")

t = Entry(top)
t.grid(row=0, columnspan=4)


def calculate(event):
    gleichung = t.get()
    t.delete(0, END)
    try:
        t.insert(0, eval(gleichung))
    except:
        t.insert(0, "invalid syntax")


B1 = Button(top, text="1")
B1.grid(row=1, column=0)
B2 = Button(top, text="2")
B2.grid(row=1, column=1)
B3 = Button(top, text="3")
B3.grid(row=1, column=2)
B4 = Button(top, text="4")
B4.grid(row=2, column=0)
B5 = Button(top, text="5")
B5.grid(row=2, column=1)
B6 = Button(top, text="6")
B6.grid(row=2, column=2)
B7 = Button(top, text="7")
B7.grid(row=3, column=0)
B8 = Button(top, text="8")
B8.grid(row=3, column=1)
B9 = Button(top, text="9")
B9.grid(row=3, column=2)
B0 = Button(top, text="0")
B0.grid(row=4, column=1)
Bplus = Button(top, text="+")
Bplus.grid(row=1, column=3)
Bminus = Button(top, text="-")
Bminus.grid(row=2, column=3)
Bmal = Button(top, text="*")
Bmal.grid(row=3, column=3)
Bdurch = Button(top, text="/")
Bdurch.grid(row=4, column=3)
Berg = Button(top, text="=")
Berg.grid(row=5, column=3)
Bdel = Button(top, text="del")
Bdel.grid(row=5, column=2)

B1.bind("<Button-1>", lambda x: t.insert(END, "1"))
B2.bind("<Button-1>", lambda x: t.insert(END, "2"))
B3.bind("<Button-1>", lambda x: t.insert(END, "3"))
B4.bind("<Button-1>", lambda x: t.insert(END, "4"))
B5.bind("<Button-1>", lambda x: t.insert(END, "5"))
B6.bind("<Button-1>", lambda x: t.insert(END, "6"))
B7.bind("<Button-1>", lambda x: t.insert(END, "7"))
B8.bind("<Button-1>", lambda x: t.insert(END, "8"))
B9.bind("<Button-1>", lambda x: t.insert(END, "9"))
B0.bind("<Button-1>", lambda x: t.insert(END, "0"))
Bplus.bind("<Button-1>", lambda x: t.insert(END, "+"))
Bminus.bind("<Button-1>", lambda x: t.insert(END, "-"))
Bmal.bind("<Button-1>", lambda x: t.insert(END, "*"))
Bdurch.bind("<Button-1>", lambda x: t.insert(END, "/"))

Berg.bind("<Button-1>", calculate)
Bdel.bind("<Button-1>", lambda x: t.delete(0, END))

top.mainloop()
