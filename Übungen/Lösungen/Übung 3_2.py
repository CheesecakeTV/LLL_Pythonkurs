
whileLaufen = True
while whileLaufen:

    eingabe = input().strip()

    if not eingabe:
        whileLaufen = False
    else:
        eingabe = int(eingabe)
        grossterTeiler = 0

        if eingabe < 0:
            print("Bitte nur positive Zahlen eingeben!")
        elif eingabe < 2:
            pass
        else:
            i = 2

            while i < eingabe:
                geteilt = eingabe / i

                if int(geteilt) == geteilt:
                    print(i,"Ja")
                    grossterTeiler = i
                else:
                    print(i,"Nein")

                i = i + 1

            if not grossterTeiler:
                print("Es ist eine Primzahl!")
            else:
                print("Größter Teiler:",grossterTeiler)
