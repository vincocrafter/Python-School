def blues(c):
    for i in range(c):
        print(i * " " + "I like Blues")


def blues2(c):
    for i in range(c):
        print("I like Blues")


def bluesneu():  # Methode blues nur mit while
    i = 0
    while (i <= 10):
        print(i * " " + "I like Blue")
        i = i - 1


def bluesneu2():  # Methode blues2 nur mit while
    i = 0
    while (i <= 14):
        print("I like Blue")
        i = i + 1

bluesneu()