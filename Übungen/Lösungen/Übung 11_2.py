
class Auto:

    def __init__(self,modelltyp:str,treibstoffverbrauch:float,gewicht:float = 0):
        self.modelltyp = modelltyp
        self.treibstoffverbrauch = treibstoffverbrauch
        self.gewicht = gewicht

    def print(self) -> None:
        print("Modeltyp:",self.modelltyp)
        print("Treibstoffverbrauch",self.treibstoffverbrauch,"l/100km")
        if self.gewicht:
            print("Gewicht:",self.gewicht,"kg")

class Elektroauto(Auto):

    def print(self) -> None:
        print("Modeltyp:",self.modelltyp)
        print("Treibstoffverbrauch",self.treibstoffverbrauch,"kWh/100km")
        if self.gewicht:
            print("Gewicht:",self.gewicht,"kg")

class Bagger(Auto):

    def __init__(self,hubkraft:float,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.hubkraft = hubkraft

    def print(self) -> None:
        super().print()
        print("Hubkraft:",self.hubkraft,"kg")


x = Bagger(1500,"Hyundai",6)
x.print()

