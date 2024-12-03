
## Übung 13.1

Erstelle den decorator `log`, welcher den Namen einer Funktion auf der Konsole ausgibt, wenn diese aufgerufen wird.

Beispiel:\
Der Code
```py
@log
def x():
    pass

@log
def y():
    pass

x()
x()
y()
```
gibt folgendes auf die Konsole aus:

> x\
> x\
> y

## Übung 13.2

Erstelle den Decorator `ExceptError`.

1. Damit soll es möglich sein, eine bestimmte Art von Fehler abzufangen, sodass das Programm nicht abstürzt (Siehe Beispiel).
2. Optional soll es möglich sein, eine Standardrückgabe zu bestimmen, welche zurückgegeben wird, wenn die Exception ausgelöst wurde.
Wird die Standardrückgabe nicht definiert, soll stattdessen None zurückgegeben werden.

```py
@ExceptError(ValueError)
def dieFkt1():
    ...

@ExceptError(ValueError,0) # 0 wird zurückgegeben, wenn ValueError ausgelöst wird
def dieFkt2():
    ...
```

## Übung 13.3

Erstelle den Decorator `cacheRuckgabe`.

Dieser speichert Ein- und Ausgabe jedes Funktionsaufrufs.
Wird die Funktion mit bereits gespeicherten Argumenten aufgerufen, soll einfach nur die vorherige Rückgabe zurückgegeben werden.
Die Funktion soll in dem Fall also nicht erneut aufgerufen werden.

Du darfst annehmen, dass die "dekorierte" Funktion keine optionalen Argumente hat.

```py
@cacheRuckgabe
def hoch(x,y):
    print("Wenn du das siehst habe ich neu berechnet")
    return x ** y

hoch(25,5) # Berechnen
hoch(25,2) # Berechnen

hoch(25,5) # Nicht berechnen, einfach vorheriges Ergebnis verwenden
```



