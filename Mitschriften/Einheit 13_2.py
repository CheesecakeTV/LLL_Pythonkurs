import math
from typing import Self
from functools import total_ordering
import json
import pickle

@total_ordering
class Vektor:

    def __init__(self,*werte:float):
        self.werte = list(werte)
        #self.grad = len(werte)
        self.halloWelt = "Hallo Welt"

    @property
    def werte(self) -> list:
        return self._werte

    @werte.setter
    def werte(self,val:list):
        self._werte = val
        self.grad = len(val)

    def __str__(self) -> str:
        return str(self.werte)

    def __len__(self) -> int:
        return self.grad

    def __add__(self, other:Self) -> Self:
        if len(self) != len(other):
            raise TypeError

        # neueWerte = []
        # for val1,val2 in zip(self.werte, other.werte):
        #     neueWerte.append(val1 + val2)
        neueWerte = [val1 + val2 for val1,val2 in zip(self.werte, other.werte)]

        return Vektor(*neueWerte)

    def __mul__(self, other:float|Self) -> float|Self:
        if isinstance(other,Vektor):
            # other ist ein Vektor
            if len(self) != len(other):
                raise TypeError

            produkte = [val1 * val2 for val1,val2 in zip(self.werte, other.werte)]

            return sum(produkte)

        # other ist eine Zahl
        neueWerte = [val1 * other for val1 in self.werte]
        return Vektor(*neueWerte)

    def __pow__(self, power, modulo=None):
        if power != 2:
            raise ValueError

        return self * self

    def __abs__(self):
        return math.sqrt(self ** 2)

    def __setitem__(self, key, value):
        self.werte[key] = value

    def __getitem__(self, item):
        return self.werte[item]

    def copy(self) -> Self:
        neuesObjekt = Vektor()
        neuesObjekt.__dict__ = self.__dict__.copy()
        return neuesObjekt

    def __lt__(self, other:Self) -> bool:
        return abs(self) < abs(other)

    def __eq__(self, other:Self) -> bool:
        return abs(self) == abs(other)

    def __bool__(self) -> bool:
        return bool(abs(self))

v1 = Vektor(2, 6, 3) # v1, v2 und v3 werden in weiteren Beispielen genutzt
v2 = Vektor(1, 2, 3)
v3 = Vektor(1, 2, 3, 4)

v4 = v1.copy()
v1.hallo = "Welt"

with open("vektor.json","w") as f:
    f.write(json.dumps(v1.__dict__, indent=4))

with open("vektor.json","r") as f:
    v5 = Vektor()
    v5.__dict__ = json.loads(f.read())

print(v5)

with open("vektor.pkl","wb") as f:
    pickle.dump([v1,v1],f)

with open("vektor.pkl","rb") as f:
    v5,v6 = pickle.load(f)

print(id(v5))
print(id(v6))

def dieFkt():
    return "Hallo","Welt"

x,y = dieFkt()
print(x)
print(y)

