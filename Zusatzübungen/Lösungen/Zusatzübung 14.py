from test import ubergange

eingabe =  [0,1,0,0,0,1,0,0,1,1,1,0,1,0,1,0,0,0,1,1,0,1,1,1,1,1,0,1,0,0,0] # Nur für Teil 1 relevant
zustande = [0,1,2,3,4,4,4,0,3,4,0,1,2,3,2,3,2,0,3,2,3,4,0,1,4,4,0,1,2,0,3] # Nur für Teil 2 relevant

# Teil 1

# [Bei 0, bei 1]
ubergange1 = [
    [3,1], # Von Zustand 0
    [2,4], # Von Zustand 1
    [0,3], # usw.
    [4,2],
    [4,0],
]

derZustand = 0
print(derZustand,end="")

for i in eingabe:
    derZustand = ubergange1[derZustand][i]
    print(" -",derZustand,end="")
print() # Neue Zeile


# Teil 2

# Eine if-Verzweigung
# Bei welchem Wechsel 1 eingegeben wurde, sonst 0
ubergange2 = [
    i[1] for i in ubergange1
]
print(ubergange2)
for jetzt,nachster in zip(zustande[:-1],zustande[1:]): # Im nächsten Teil ist eine weitere Möglichkeit die Schleife zu durchlaufen
    if ubergange2[jetzt] == nachster:
        print("1 - ",end="")
    else:
        print("0 - ",end="")
print("?")

# Ohne if-Verzweigungen
# [Bei 0, bei 1, usw.]
ubergange2 = [
    [0,1,0,0,0],
    [0,0,0,0,1],
    [0,0,0,1,0],
    [0,0,1,0,0],
    [1,0,0,0,0],
]

for n,_ in enumerate(zustande[:-1]): # Alternativ: for n in range(len(eingabe) - 1):...
    print(ubergange2[zustande[n]][zustande[n + 1]], end=" - ")
print("?")


# Teil 3

derZustand = 0
while True:
    nutzerEingabe = input().strip()

    if not nutzerEingabe:
        break

    for i in nutzerEingabe:
        if not i in ["0","1"]:
            continue

        derZustand = ubergange1[derZustand][int(i)]
        print("Zustand:",derZustand)


