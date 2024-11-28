
passworter = [
    ["Hallo","Eric"],
    ["Welt","Tobias"],
    ["Discord","Chris"],
    ["LLL","Server"]
]


versuche = 3
nutzername = ""

while not nutzername:
    if versuche == 0:
        print("Keine Versuche übrig!")
        exit()

    i = 0

    eingabe = input()

    while i < len(passworter):
        if eingabe == passworter[i][0]:
            nutzername = passworter[i][1]
            i = 1000 # Schleife beenden

        i += 1

    versuche -= 1

print("Zugang erfolgreich.")
print("Nutzername:",nutzername)


