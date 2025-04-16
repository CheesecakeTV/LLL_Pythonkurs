import time
import threading

zahler = 0

def fkt1():
    global zahler
    while True:
        print("Hallo Welt", zahler)
        zahler += 1
        time.sleep(0.5)

def fkt2():
    global zahler
    while True:
        print("Hallo Discord",zahler)
        zahler += 1
        time.sleep(1)

t1 = threading.Thread(target=fkt1,daemon=True)
t2 = threading.Thread(target=fkt2,daemon=True)

t1.start()
time.sleep(0.1)
t2.start()

input()

