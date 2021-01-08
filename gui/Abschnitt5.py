# von
# https://praxistipps.chip.de/python-gui-programmierung-das-muessen-sie-wissen_95044

from tkinter import *

import tkinter


def test1():
    print("Test1")


root = Tk()

root.title("Test")

button1 = Button(text="Test", bg="white", fg="black", command=test1)
button1.grid()

var1 = IntVar()

checkbutton1 = Checkbutton(root, text="Test", onvalue=1, offvalue=0, variable=var1)
checkbutton1.grid()

radiobutton1 = Radiobutton(root, text="Test", value=1)
radiobutton1.grid()

root.mainloop()
