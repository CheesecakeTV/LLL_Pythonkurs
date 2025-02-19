
class Test:

    def __init__(self,name:str):
        print("Hallo Welt")
        self.meinName = name

    def printName(self):
        print(self.meinName)

x = Test("Test")
y = Test("Discord")

x.printName()
y.printName()

print(isinstance(x,Test))
print(isinstance(x,int))
print(type(x) == Test)

