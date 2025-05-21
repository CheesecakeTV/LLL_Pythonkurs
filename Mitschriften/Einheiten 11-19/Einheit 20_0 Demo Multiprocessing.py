import multiprocessing
import math
import time
import threading

def nutzloseFkt(startwert:int):
    while True:
        startwert = startwert ** 2
        startwert += 1
        startwert = math.sqrt(startwert)
        startwert -= 1

if __name__ == "__main__":
    for i in range(2,18):
        multiprocessing.Process(target=nutzloseFkt,args=(i,),daemon=True).start()
        #threading.Thread(target=nutzloseFkt,args=(i,),daemon=True).start()

    time.sleep(15)
