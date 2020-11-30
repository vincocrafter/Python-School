n = int(input("Primzahl: "))
t = 0
i = 1

while(i <= n):
    if(n % i == 0):
        t = t + 1
    i = i + 1
if(t == 2):
    print(n, " ist eine Primzahl")
else:
    print(n, " ist Keine Primzahl")
