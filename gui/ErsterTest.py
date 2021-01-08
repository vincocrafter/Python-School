#von
#https://praxistipps.chip.de/python-gui-programmierung-das-muessen-sie-wissen_95044

from tkinter import *

import tkinter


def save():
    print("Save")


root = Tk()

root.title("Test")

menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)

filemenu.add_command(label="Speichern", command=save)
filemenu.add_separator()
menubar.add_cascade(label="Datei", menu=filemenu)

root.config(menu=menubar)
root.mainloop()
