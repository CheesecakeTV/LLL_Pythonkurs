
dieListe = []
eingabe = "Hallo"

while eingabe:
    eingabe = input().strip()

    if eingabe:
        dieListe.append(int(eingabe))


dieListe.sort()
del dieListe[-1]
dieListe = dieListe[::-1]

i = 0
summe = 0
while i < len(dieListe):
    summe += dieListe[i]
    print(dieListe[i],summe,sep=" - ")
    i += 1 # i = i + 1




