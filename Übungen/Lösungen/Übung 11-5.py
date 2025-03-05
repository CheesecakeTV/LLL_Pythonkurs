
# 1.
def dieFunktion(abstandZu:int):
   return lambda a:abs(abstandZu - a)

# Ab hier nichts ändern!!!
x = [1, 65, 7, 3, 4, 2, 3, 6, 8, 43, 4, -2, -10, 5, 2, -13]
x.sort(key=dieFunktion(5))
print("Abstand zu 5:", x)
x.sort(key=dieFunktion(10))
print("Abstand zu 10:", x)
x.sort(key=dieFunktion(-3))
print("Abstand zu -3:", x)


# 2.
loggen = True
def log(zuLoggen:any, vortext:str="") -> any:
    if loggen:
        print(f"{vortext}{zuLoggen}")
    return zuLoggen

x = log(5) # x wird auf 5 gesetzt und “5” wird auf der Konsole ausgegeben.

# 3.
def istAhnlich(derText:str, suchtext:str) -> bool:
    derText, suchtext = derText.casefold(), suchtext.casefold()

    if suchtext in derText:
        return True

    if len(suchtext) < 2:
        return False

    for n in range(len(suchtext)):
        splittext = suchtext[:n] + suchtext[n + 1:]
        if splittext in derText:
            return True

    return False

print(istAhnlich("HalloWelt","Halllo"))
print(istAhnlich("HalloWelt","Hallo Welt"))
