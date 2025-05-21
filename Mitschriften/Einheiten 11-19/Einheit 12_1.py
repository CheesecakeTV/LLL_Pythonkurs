
class meinInt:

    def __init__(self,wert):
        self.wert = wert

    def __add__(self, other):
        if not isinstance(other,meinInt):
            return NotImplemented

        return meinInt(self.wert + other.wert)

    def __str__(self) -> str:
        return "meinInt: " + str(self.wert)

    def __radd__(self, other:int):
        return meinInt(other + self.wert)

    # def __repr__(self) -> str:
    #     return "repr" + str(self.wert)

    def __format__(self, format_spec:str) -> str:
        print("Format!",format_spec)
        return str(self.wert)

    def __enter__(self):
        print("Enter",self.wert)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exit",self.wert)

        if exc_type == ZeroDivisionError:
            return 1

x = meinInt(5)
y = meinInt(6)

# print(x)
# print(x + y)
#
# print(5 + x)
# x += y
#
# print(f"{x:HalloWelt}")


# x = 2.1234
# print(f"{x:.2f}")
# x = 100000000000
# print(f"{x:_}")



