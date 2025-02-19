
def meineFkt(dieZahl:int) -> bool:
    if not isinstance(dieZahl, int):
        raise TypeError("Nur int übergeben!")

    if dieZahl < 0:
        raise ValueError("Der Wert muss größer 0 sein")

    assert dieZahl != 0,"Der Wert muss größer 0 sein"

    return False

