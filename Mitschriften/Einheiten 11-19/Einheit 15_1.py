
def fkt(meinParam:callable):
    """
    Hallo Discord!
    :param meinParam:
    :return:
    """
    meinParam()

def fkt2():
    print("Hallo Welt")

def fkt3() -> callable:
    discord = 0
    def hallo():
        nonlocal discord
        print(discord)
        discord += 1
    return hallo

