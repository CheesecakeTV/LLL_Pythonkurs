

#raise ArithmeticError("Das ist ein Test")
#assert True
# if True:
#     raise AssertionError

def dieFkt(derParam:float) -> None:
    assert isinstance(derParam,(int,float)), "Das ist ein Test"

dieFkt(15)
dieFkt("Hallo")
#dieFkt(15.5)

try:
    x = int(input())
    print("Ok")
    print(1 / x)
except ValueError:
    print("Es wurde keine Zahl eingegeben")
except ZeroDivisionError:
    print("Es wurde 0 eingegeben")
except Exception as ex:
    print(str(ex))
    print(ex.__class__.__name__)


print("Fertig")


