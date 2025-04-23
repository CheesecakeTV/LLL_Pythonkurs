import threading
import time
import random

dieBarrier = threading.Barrier(5)

def fkt():
    time.sleep(random.randint(1,6))
    print("Fertig1!")
    dieBarrier.wait()
    time.sleep(random.randint(1,6))
    print("Fertig2!")
    dieBarrier.wait()

t1 = threading.Thread(target=fkt,daemon=True)
t2 = threading.Thread(target=fkt,daemon=True)
t3 = threading.Thread(target=fkt,daemon=True)
t4 = threading.Thread(target=fkt,daemon=True)

t1.start()
t2.start()
t3.start()
t4.start()

dieBarrier.wait()
dieBarrier.wait()

exit()

t1.join()
t2.join()
t3.join()
t4.join()
