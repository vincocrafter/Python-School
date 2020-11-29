def opendat(path, name, type):  # Öffent immer die Datei und Läd sie
    if name == 0 or name == "": # Überprüft ob der Name ungültig ist
        print("Name ungültig")
        exit()
    datei = path + name
    try:
        in_file = open(datei, type)
    except Exception:
        print("Fehler beim öffenen der Datei")
        return None  # Wenn ein Fehler passiert gibt er none zurück
    else:
        return in_file


def readdat(name):
    file = opendat("./", name, "r")
    text = file.read()
    return text


def writedat(name, content):
    file = opendat("./", name, "w")
    file.write(content)


def writeLine(name, content):
    writedat(name, "\n" + content)
