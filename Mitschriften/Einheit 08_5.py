
def dieFkt(x:int):
    # Rekursionsverankerung
    # Ende der Rekursion
    if x < 0:
        return # Beende die Funktion

    # Rekursionsschritt
    print(x)
    dieFkt(x - 1)

def fakultaet(x):
    # 5! = 1 * 2 * 3 * 4 * 5
    if x == 0: # Rekursionsverankerung
        return 1

    return x * fakultaet(x - 1) # Rekursionsschritt

print(fakultaet(5))
