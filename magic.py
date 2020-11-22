def muster():
    print('*'*7)
    print('*' + ' '*5 + '*')
    print('*'*7)


def magic(name):
    wort = input("Nenne das Zauberwort : ")
    if wort == "HokusPokus":
        print(name + ", du wirst zum Zaubermeister ernannt!")
    else:
        print("Du wirst verzaubert, Donald Duck")

magic("Vincent")

