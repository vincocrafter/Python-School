def passwort():
    i = 1
    eingabe = ""
    while (i <= 3 and eingabe != "GEHEIM"):
        # hier beginnt die Schleife
        print("Passwortabfrage (", i, ".ter Versuch)")
        eingabe = input("Passwort: ")
        if (eingabe == "GEHEIM"):
            print("Wir begruessen dich am Rechner Athena2222!")
        elif (i == 3):
            print("SO wirst du NIE das Passwort erraten!")
        else:
            print("Falsches Passwort zur falschen Zeit am falschen Ort!")
        i = i + 1


def passwort2():
    i = 1
    eingabe = ""
    while (i <= 3 and eingabe != "GEHEIM"):
        # hier beginnt die Schleife
        print("Passwortabfrage (", i, ".ter Versuch)")
        eingabe = input("Passwort: ")
        if (eingabe == "GEHEIM"):
            print("Wir begruessen dich am Rechner Athena2222!")
        elif (i == 3):
            print("SO wirst du NIE das Passwort erraten!")
        else:
            print("Falsches Passwort zur falschen Zeit am falschen Ort!")
        i = i - 1  # Zählervariable umgedreht Also i wird immer kleiner


passwort2()
