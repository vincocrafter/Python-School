# Information von mit Konstanter Größe von https://www.delftstack.com/de/howto/python-tkinter/how-to-create-a-tkinter-window-with-a-constant-size/

# Geklaute Methoden aus basics/A12_Viewer.py

from tkinter import *

# Definition für das HauptGUI
from tkinter import Tk

gui = Tk()


def opendat(path, name, type):  # Methode zur öffung einer Datei
    if len(name) == 0 or name == "" or name == None:  # Überprüft ob der Name ungültig ist
        print("Name ungültig")
        exit()
    datei = path + name
    try:  # Ausnahmehandlung falls es einen Fehler gibt
        in_file = open(datei, type)
    except Exception:
        print("Fehler beim öffenen der Datei")
        return None  # Wenn ein Fehler passiert gibt er none zurück
    else:
        return in_file


def readdat(name):
    file = opendat("../../", name,"r")  # Da die Dateiöffnung mehrfach benötigt wird habe ich es als Methode definiert --> Code ersparnis
    if (file != None):
        text = file.read()
        return text


def writedat(name, content):
    file = opendat("../../", name,"w")  # Da die Dateiöffnung mehrfach benötigt wird habe ich es als Methode definiert --> Code ersparnis
    if (file != None):
        file.write(content)


def writeLine(name, content):
    writedat(name, "\n" + content)


# Methodendeklarationen für Programm


def save():
    print("Save")


opengui = None


def save2():
    # Öffnen
    gui.quit()


    opengui = Tk()
    opengui.title("Datei Öffnen: ")

    opengui.geometry("500x100")
    opengui.resizable(width=0, height=0)

    a = Label(text="Dateiname:", bg="white", fg="black")
    a.grid()

    back = Button(text="Zurück", bg="white", fg="black", command=shutdownopenFile)
    back.place(x=100, y=100)
    back.grid()

    b = Entry()
    b.grid(row=40, column=1, sticky=W)

#    b.pack(side='top', fill='x', padx='5', pady='10')

    print(b.info)

    opengui.mainloop()


def shutdown():
    exit()


def shutdownopenFile():
    opengui.quit()
    opengui.destroy()
    startGUI()


def startGUI():
    gui = Tk()
    gui.title("Dateimanager")

    gui.geometry("400x400")
    gui.resizable(width=1, height=1)

    menubar = Menu(gui)

    # Speichern
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Speichern", command=save)
    filemenu.add_command(label="Speichern unter", command=save2)
    filemenu.add_separator()
    filemenu.add_command(label="Programm Beenden", command=shutdown)

    menubar.add_cascade(label="Datei", menu=filemenu)

    # Neues Menü
    editmenu = Menu(menubar, tearoff=0)

    editmenu.add_separator()

    gui.config(menu=menubar)
    gui.mainloop()


startGUI()
