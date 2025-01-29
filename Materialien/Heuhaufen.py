import random as r

# r.seed(0) # Einfügen, um stets den selben Heuhaufen zu erhalten

maxTiefe = 2    # Die maximale Tiefe
einheitlicheTiefe = True # Ob die Tiefe (nicht) zufällig ist
maxStrangeProKnoten = 10 # Wie viele Unterknoten jeder Knoten haben soll
heuhaufenPrinten = True # Ob der Heuhaufen auf die Konsole ausgegeben werden soll

print("Hier ist die Nadel: ", end="")

def gibUnterknoten(tiefe=0, duHastNadel=True):
    if tiefe >= maxTiefe:
        if duHastNadel:
            print("Nadel")
            return "Nadel"
        return "Heu"

    if not einheitlicheTiefe:
        tiefe += r.randint(tiefe, maxTiefe + 1) == tiefe

    ruckgabe = []
    knotenZahl = r.randint(1,maxStrangeProKnoten)

    if duHastNadel:
        nadel = r.randint(0,knotenZahl)
        print(nadel, end=" - ")
    else:
        nadel = -1

    for i in range(knotenZahl + 1):
        ruckgabe.append(gibUnterknoten(tiefe=tiefe + 1, duHastNadel=(i == nadel)))

    return ruckgabe

heuhaufen = gibUnterknoten()

# Heuhaufen ausgeben
print("\nDas ist dein Heuhaufen:\n" * heuhaufenPrinten,end="")
for i in heuhaufen * heuhaufenPrinten:
    print(i)

# Kontrolle, damit du dich nicht tot-suchst und nachher doch keine Nadel erzeugt wurde
print("\nHeuhaufen enthält eine Nadel:","Ja" if "Nadel" in str(heuhaufen) else "Nein")


### Der erzeugte Heuhaufen wurde in der Variable "heuhaufen" gespeichert ###
### Ab hier darfst du Code hinzufügen ###


