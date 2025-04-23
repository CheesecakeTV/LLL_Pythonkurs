import threading


def dieFkt():
    print("Hallo Welt")

threading.Timer(3,function=dieFkt).start()
threading.Timer(5,function=dieFkt).start()


