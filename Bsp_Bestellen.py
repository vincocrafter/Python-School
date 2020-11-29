menge = int(input("Nenne bitte die Menege: "))

if(menge >= 100):
    r = 10
elif(menge >= 50):
    r = 7
elif(menge >= 10):
    r = 5
else:
    r = 0

print("Rabatt :" + str(r))