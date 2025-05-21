from functools import wraps

class Katze:
    def __init__(self,name:str,geburtsjahr:int,geschlecht:str):
        """
        Hallo Welt
        :param name:
        :param geburtsjahr:
        :param geschlecht:
        """
        self.name = name
        self.geburtsjahr = geburtsjahr
        self.geschlecht = geschlecht

        self.vorname, self.nachname = name.split()

    def getAlter(self,jahr:int) -> int:
        return jahr - self.geburtsjahr

    def print(self):
        print(f"Name:\t\t\t{self.name}")
        self.dazwischen()
        print(f"Geburtsjahr:\t{self.geburtsjahr}")
        print(f"Geschlecht:\t\t{self.geschlecht}")

        # if self.ehepartner:
        #     print(f"Ehepartner:\t\t{self.ehepartner.name}")

    def dazwischen(self):
        ...

class Person(Katze):
    # def __init__(self,name:str,geburtsjahr:int,geschlecht:str):
    #     super().__init__(name,geburtsjahr,geschlecht)

    #@wraps(Katze.__init__)
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.ehepartner = None

    #__init__.__doc__ = Katze.__init__.__doc__

    def heirate(self,diePerson) -> None:
        self.ehepartner = diePerson
        diePerson.ehepartner = self

    def dazwischen(self):
        # Hier könnte man was in die Methode print einfügen
        ...

x = Person("Hallo Welt",2000,"M")
x.print()


