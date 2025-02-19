from typing import Self

allePersonen = []

class Person:
    def __init__(self,name:str,geburtsjahr:int,geschlecht:str):
        self.name = name
        self.geburtsjahr = geburtsjahr
        self.geschlecht = geschlecht

        self.vorname, self.nachname = name.split()

        self.ehepartner = None

        allePersonen.append(self)

    def getAlter(self,jahr:int) -> int:
        return jahr - self.geburtsjahr

    def print(self):
        print(f"Name:\t\t\t{self.name}")
        print(f"Geburtsjahr:\t{self.geburtsjahr}")
        print(f"Geschlecht:\t\t{self.geschlecht}")

        if self.ehepartner:
            print(f"Ehepartner:\t\t{self.ehepartner.name}")

    def heirate(self,diePerson:Self) -> None:
        self.ehepartner = diePerson
        diePerson.ehepartner = self


personA = Person("Walter Frei", 1980, "M")
personB = Person("Marie Steinke", 1985, "W")
personA.heirate(personB)

personB.print()
print(allePersonen)