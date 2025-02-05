
x = [1,2,3,4,5,6]

def hoch2(element:float) -> float:
    return element ** 2

def istDurch2Teilbar(element:float) -> bool:
    return element % 2 == 0

y = list(map(hoch2,x))
print(y)

y = list(filter(istDurch2Teilbar,x))
print(y)

# lambda [Parameter] : [Rückgabe]
dieLambda = lambda element:element % 2 == 0
y = list(filter(lambda element:element % 2 == 0,x))

