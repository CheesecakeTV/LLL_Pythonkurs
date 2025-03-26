from functools import wraps

def derDec(fkt):
    counter = 0

    @wraps(fkt)
    def ruckgabe(*args,**kwargs):
        nonlocal counter
        counter += 1
        print(counter)
        return fkt(*args,**kwargs)
    return ruckgabe

@derDec
def fak(zahl1):
    """
    Fakultät berechnen
    :param zahl1:
    :return:
    """
    ruckgabe = 1
    for i in range(1,zahl1 + 1):
        ruckgabe *= i

    return ruckgabe

print(fak(5))
print(help(fak))

exit()

@derDec
def testFkt(hallo):
    print("testFkt")

@derDec
def testFkt2():
    print("testFkt2")

testFkt("Welt")
testFkt("Welt")
testFkt("Welt")
testFkt2()
testFkt("Welt")
testFkt2()
testFkt("Welt")
