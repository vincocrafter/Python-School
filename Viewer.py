def opendat(path, name, type):
    if name == 0 or name == "":
        print("Fehler 1")
        exit()
    datei = path + name
    try:
        in_file = open(datei, type)
    except Exception:
        print("Fehler beim öffenen der Datei")
        return None
    else:
        return in_file


def readdat(name):
    file = opendat("./", name, "r")
    text = file.read()
    return text


def writedat(name, content):
    file = opendat("./", name, "w")
    file.write(content)

def writeLine(name,content):
    writedat(name,"\n" + content)
