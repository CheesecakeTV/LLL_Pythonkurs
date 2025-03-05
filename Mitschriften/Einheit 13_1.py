

class Test:

    def __init__(self):
        self._hallo = None

    @property
    def hallo(self): # Getter
        return self._hallo

    @hallo.setter
    def hallo(self,val):
        self._hallo = val

    @hallo.deleter
    def hallo(self):
        print("Delete")

x = Test()
x.hallo = "Welt"
print(x.hallo)
