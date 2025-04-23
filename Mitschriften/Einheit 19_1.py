import threading
import time

dasLock = threading.Lock()
#dasLock = threading.Semaphore(2)

def fkt2(zahler):
    while True:
        #dasLock.acquire()
        with dasLock:
            for i in "Hallo Discord":
                print(i,end="")
                time.sleep(0.01)
            print(zahler)
        #dasLock.release()
        zahler[0] += 1
        time.sleep(1)

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

input()