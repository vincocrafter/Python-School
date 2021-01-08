# von
# https://praxistipps.chip.de/python-gui-programmierung-das-muessen-sie-wissen_95044

from tkinter import *

import tkinter


# Methodendefinitionen
# Da sonst die add_command Methode probleme hat (Methode save wird dann ausgeführt)
def save():
    print("Save")


def save2():
    print("Save")


def shutdown():
    print("Shutdown")


def undo():
    print("Rückgänig")


def redo():
    print("Redo")


root = Tk()

root.title("Test")

menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Speichern", command=save)
filemenu.add_command(label="Speichern unter", command=save2)
filemenu.add_separator()
filemenu.add_command(label="Programm Beenden", command=shutdown)

menubar.add_cascade(label="Datei", menu=filemenu)

# Neues Menü
editmenu = Menu(menubar, tearoff=0)

editmenu.add_command(label="Rückgänig", command=undo)
editmenu.add_separator()
editmenu.add_command(label="Wiederholen", command=redo)

menubar.add_cascade(label="Bearbeiten", menu=editmenu)

root.config(menu=menubar)
root.mainloop()
