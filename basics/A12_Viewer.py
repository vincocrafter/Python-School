# Die Save first Methode
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
    file = opendat("../../", name, "r")  # Da die Dateiöffnung mehrfach benötigt wird habe ich es als Methode definiert --> Code ersparnis
    if (file != None):
        text = file.read()
        return text


# Schreibe Datei Methode
def writedat(name, content):
    file = opendat("../../", name,
                   "w")  # Da die Dateiöffnung mehrfach benötigt wird habe ich es als Methode definiert --> Code ersparnis
    if (file != None):
        file.write(content)


def writeLine(name, content):
    writedat(name, "\n" + content)
