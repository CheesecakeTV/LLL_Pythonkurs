import time
import threading

def istPrim(dieZahl:int) -> bool:
    time.sleep(3)
    for i in range(2,dieZahl):
        if dieZahl % i == 0:
            print(dieZahl,"ist keine Primzahl!")
            return False

    print(dieZahl, "ist eine Primzahl!")
    return True

while True:
    eingabe = int(input().strip())

    threading.Thread(target=istPrim,args=(eingabe,)).start()

