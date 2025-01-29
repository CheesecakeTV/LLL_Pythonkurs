
def test(dieListe:list[int | float]) -> None:
    """
    Das ist ein Test
    :param dieListe: Irgendeine Liste
    :return: Keine Rückgabe
    """
    dieListe = dieListe.copy()
    dieListe[0] = 15
    print(dieListe)

print(help(test))

def mitTypehints(dieListe:list|tuple) -> list|tuple:
    return dieListe

def verarbeiteDict(dasDict:dict[str:int] = None):
    pass

x = [1,2,3,4,5]
#test(x)
#print(x)

def hochZwei(x):
    return x ** 2

def hoch(x):
    return x ** 2, x ** 3, x ** 4

y,z,a = hoch(5)
print(y)
print(z)
print(a)
