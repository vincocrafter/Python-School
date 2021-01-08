# von
# https://praxistipps.chip.de/python-gui-programmierung-das-muessen-sie-wissen_95044

from tkinter import *

import tkinter


root = Tk()

root.title("Test")

b = Entry()
b.grid(row=40, column=1, sticky=W)

b.pack(side='top', fill='x', padx='5', pady='10')

root.mainloop()
