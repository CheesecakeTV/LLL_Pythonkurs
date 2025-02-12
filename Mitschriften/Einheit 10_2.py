
class DieKlasse:

    def __init__(self,hallo=None):
        self.hallo = hallo

    def dieMethode(self):
        print("Hallo Welt")
        print(self.hallo)

x = DieKlasse()
#x.dieMethode()
x.hallo = "Welt"
x.dieMethode()

y = DieKlasse()
y.dieMethode()
print(id(x))
print(id(y))

# y = DieKlasse()
# y.hallo = "Discord"
# y.dieMethode()
#
# z = DieKlasse("Hallo Sellerie")
# z.dieMethode()

# print(isinstance(x,DieKlasse))


