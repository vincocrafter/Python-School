def kreuz():
    print(" " * 2 + "##" + " " * 2)
    print(" " * 2 + "##" + " " * 2)
    print("#" * 6)
    print(" " * 2 + "##" + " " * 2)
    print(" " * 2 + "##" + " " * 2)


#Kreuz mit for schleifen
def kreuzneu():
    for i in range(2):
        print(" " * 2 + "##")
    for i in range(2):
        print("#" * 6)
    for i in range(2):
        print(" " * 2 + "##")


kreuzneu()
kreuz()
