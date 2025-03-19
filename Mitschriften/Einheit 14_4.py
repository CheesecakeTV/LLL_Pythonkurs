from typing import Iterator,Iterable

x = [15,23,6,23,7,2,3,6,2,3]

for n,i in enumerate(x):
    ...
    #print(n,i)

def meinEnumerate(elem:Iterable) -> tuple:
    i = 0
    for dasElement in elem:
        yield i,dasElement
        i += 1

for n,i in meinEnumerate(x):
    print(n,i)
