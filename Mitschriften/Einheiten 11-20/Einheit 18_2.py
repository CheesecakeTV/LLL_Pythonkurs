import time
import threading


def fkt1(zahler):
    while True:
        print("Hallo Welt", zahler)
        zahler[0] += 1
        time.sleep(0.5)

def fkt2(zahler):
    while True:
        for i in "Hallo Discord":
            print(i,end="")
            time.sleep(0.01)
        print(zahler)
        zahler[0] += 1
        time.sleep(1)

zahler = [0]
t1 = threading.Thread(target=fkt1,daemon=True,args=(zahler,))
t2 = threading.Thread(target=fkt2,daemon=True,args=(zahler,))

t1.start()
t2.start()

input()

