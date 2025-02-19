
def pi() -> float:
    return 3.14159265359

def durchschnitt(a:float, b:float) -> float:
    return (a + b)/ 2

def durchschnitt_i(*werte:float) -> float:
    summe = 0
    for i in werte:
        summe += i

    return summe / len(werte)

def listeAusgeben(dieListe:list) -> None:
    for n,i in enumerate(dieListe):
        print(n,i)

def maximum(dieListe:list[float]) -> float:
    dasMax = dieListe[0]
    for i in dieListe:
        if dasMax < i:
            dasMax = i
    return dasMax

def swap(dieListe:list) -> None:
    # Mit Unpacking: dieListe[0],dieListe[-1] = dieListe[-1],dieListe[0]
    temp = dieListe[-1]
    dieListe[-1] = dieListe[0]
    dieListe[0] = temp

def setzeElemente(dasDict:dict,**neueWerte) -> None:
    #Einfacher: dasDict.update(neueWerte)
    for key,val in neueWerte.items():
        dasDict[key] = val

def splitTwice(derString:str, char1:str, char2:str) -> list[list[str]]:
    temp = derString.split(char1)
    return [i.split(char2) for i in temp]

    # Aufwändiger:
    ruckgabe = []
    for i in temp:
        ruckgabe.append(i.split(char2))
    return ruckgabe

