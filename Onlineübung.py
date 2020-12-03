a = int(input("Zahl her: "))

i = 1
zähler = 0
while (0 < i < a):
    if (a % i == 0):
        zähler = zähler + 1
    i = i + 1

if (zähler > 2):
    print(a, "ist keine Primzahl")
else:
    print(a, "ist eine Primzahl")