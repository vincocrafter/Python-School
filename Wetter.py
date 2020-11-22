pressure = input("Luftdruck: ")
temp = input("Lufttemperatur:")
season = input("Jahreszeit:")

if pressure == "steigt" and temp == "steigt" and season == "Sommer":
    print("Pack die Badehose ein, nimm dein kleines Schwesterlein...")
elif pressure == "steigt" and temp == "Fällt" and season == "Winter" :
    print("Hei, hei, hei, so eine Schneeballschlacht...")
elif pressure == "fällt" and temp == "steigt" and season == "Sommer" :
    print("Hei, hei, hei, so eine Schneeballschlacht...")
elif pressure == "fällt" and temp == "fällt" and season == "Winter" :
    print("Leise rieselt der Schnee...")
else:
    print("Nichts Genaues weiß man nicht!")

# Überprüfung Eingaben
# Überprüft ob die Eingaben in Ordnung sind und ob die zu den auswählbaren Eingaben gehören
#if pressure != "steigt" and pressure != "fällt":
#    print("Ungültiger Luftdruck")
#    exit()
#if temp != "steigt" and temp != "fällt":
#    print("Ungültige Temperatur")
#    exit()
#if season != "Sommer" and season != "Herbst" and season != "Winter" and season != "Frühling":
#    print("Ungültige Jahreszeit!")
#    exit()
