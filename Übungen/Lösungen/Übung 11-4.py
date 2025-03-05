import math
from typing import Self
from functools import total_ordering

@total_ordering
class Vektor:

    def __init__(self,*werte:float):
        self.werte = list(werte)
        #self.grad = len(werte)

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
        return Vektor(*self.werte)

    def __lt__(self, other:Self) -> bool:
        return abs(self) < abs(other)

    def __eq__(self, other:Self) -> bool:
        return abs(self) == abs(other)

    def __bool__(self) -> bool:
        return bool(abs(self))

v1 = Vektor(2, 6, 3) # v1, v2 und v3 werden in weiteren Beispielen genutzt
v2 = Vektor(1, 2, 3)
v3 = Vektor(1, 2, 3, 4)
