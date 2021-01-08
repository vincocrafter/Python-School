# Aufgabe 1
umsatz = int(input("Bitte nennen sie den Umsatz ihrer Abteilung: "))

prämieprozent = 0
prämie = 0

if (umsatz >= 50_000):
    prämieprozent = 3
    prämie = umsatz * 0.03
elif (umsatz >= 40_000):
    prämieprozent = 2
    prämie = umsatz * 0.02
elif (umsatz >= 30_000):
    prämieprozent = 1
    prämie = umsatz * 0.01
else:  # Else block kann Weggelassen werden
    prämieprozent = 0
    prämie = 0

print("Prozentwert : " + str(prämieprozent))
print("Prämie : " + str(prämie))


# Aufgabe 3 A)
# Mir ist bewusst das es so nicht Geplant ist, ich wusste nur nicht wie sonst ohne Listen
# Format -> ... ,Kontostand, ....

def konto():
    kontoliste = input("Nenne bitte deine Kontoliste: ")
    zinsen = 0
    kontostandneu = 0
    listeneu = ""
    i = 0
    while (i < len(kontoliste.split(","))):  # Arbeiten mit Abschnitten, [kein Plan wie sonst ohne Liste sry]
        kontostand = float(kontoliste.split(",")[i])  # Erkennung des Kontostandes
        if (kontostand >= 1000):
            zinsen = kontostand * 0.01
            kontostandneu = kontostand + zinsen
        else:
            zinsen = kontostand * 0.02
            kontostandneu = kontostand + zinsen
        listeneu = listeneu + str(kontostandneu) + ", "
        i = i + 1
    print(listeneu)


# A3 b)
# Format -> ... ,Kontoinhaber:Kontostand, ....
def abfrage(besitzername):
    kontoliste = input("Nenne bitte deine Kontoliste: ")
    i = 0
    while (i < len(kontoliste.split(","))):  # Arbeiten mit Abschnitten, [kein Plan wie sonst ohne Liste sry]
        info = kontoliste.split(",")[i]  # Erkennung der Abschnitte
        name = info.split(":")[0]  # Erkennung des Namens
        if (name == besitzername):
            kontostand = float(info.split(":")[1])  # Erkennung des Kontostandes
            print("Konto : " + name)
            print("Kontostand : " + str(kontostand))
        i = i + 1


# Aufgabe 3 richtig

i = 0
while (i <= 6):
    kontostand = float(input("Nenne deinen Tabellenwert: "))
    if (kontostand >= 1000):
        zinsen = kontostand * 0.01
        kontostandneu = kontostand + zinsen
    else:
        zinsen = kontostand * 0.02
        kontostandneu = kontostand + zinsen
    print("Kontostandneu : " + str(kontostandneu))
    i = i + 1
