from time import sleep

x = 0
while True:
    sleep(0.1)

    x += 1

    if x == 8:
        continue # Überspringt den aktuellen Schleifen-Durchlauf

    print(x)

    if x > 10:
        break # Aus der Schleife springen







