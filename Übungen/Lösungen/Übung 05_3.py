
eingabe = "Hi"
while eingabe:
    eingabe = input()

    if not eingabe:
        pass
    elif eingabe[::2] == eingabe[1::2][::-1]: # Test ob Eingabe bereits verschlüsselt ist

        # Entschlüsseln

        entschlusselt = eingabe[::2]
        print("Entschlüsselt:",entschlusselt)

    else:
        # Verschlüsseln
        # Auf dieses Lösung hier zu kommen ist schwierig, also mach dir nichts draus wenn du Schleifen dafür nutzt.

        dieListe = list(eingabe * 2) # Liste mit doppelter Länge wie die Eingabe, die Elemente darin sind erstmal egal
        dieListe[::2] = eingabe
        dieListe[1::2] = eingabe[::-1]
        verschlusselt = "".join(dieListe)

        print("Verschlüsselt:",verschlusselt)






