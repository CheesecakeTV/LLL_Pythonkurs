def dieFunktion_1(a:int)->int:
	return abs(a)

def dieFunktion_2(a:int)->int:
    return a

def dieFunktion_3(a:int)->int:
    return -a

def dieFunktion_4(a:int)->int:
    if not a: # a == 0
        return 10001
    return a # Ansonsten

# Unter dieser Zeile nichts verändern!!!
x = [1, 5, 3, -41, -7, 5, 0, -4, 89, -2, 1234, 3, 0, 6, -4, 1, -2, 5, 10, -25, 103]
print(list(map(dieFunktion,x))) # Für dich als Hilfe
x.sort(key=dieFunktion)
print(x)