import threading
import time

dasLock = threading.Lock()
dasEvent = threading.Event()
#dasLock = threading.Semaphore(2)

def fkt2(zahler):

    with dasLock:
        dasEvent.wait()
        #dasEvent.clear()

        for i in "Hallo Discord":
            print(i,end="")
            time.sleep(0.01)
        print()

zahler = [0]
t1 = threading.Thread(target=fkt2,daemon=True,args=(zahler,))
t2 = threading.Thread(target=fkt2,daemon=True,args=(zahler,))
threading.Thread(target=fkt2,daemon=True,args=(zahler,)).start()
threading.Thread(target=fkt2,daemon=True,args=(zahler,)).start()
threading.Thread(target=fkt2,daemon=True,args=(zahler,)).start()
threading.Thread(target=fkt2,daemon=True,args=(zahler,)).start()
threading.Thread(target=fkt2,daemon=True,args=(zahler,)).start()
threading.Thread(target=fkt2,daemon=True,args=(zahler,)).start()

t1.start()
t2.start()

time.sleep(1)
dasEvent.set()
time.sleep(1)
dasEvent.set()
time.sleep(1)
dasEvent.set()
time.sleep(1)
dasEvent.set()

input()


