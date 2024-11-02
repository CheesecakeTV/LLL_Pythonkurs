
## Übung 9.1

Die Teilaufgaben sind unabhängig voneinander lösbar.\
Implementiere folgende Funktionen. Füge bei jeder Funktion alle Typehints hinzu.

1. pi(): Gibt 3.14159265359 zurück 
2. durchschnitt(a,b): Gibt den durchschnitt von a und b zurück. Den Durchschnitt berechnet man, indem man alle Elemente zusammenaddiert und durch die Anzahl an Elementen teilt. In dem Fall also (a + b) : 2. 
   1. Optional: Die Funktion soll unendlich viele Argumente annehmen können. Z.B.: durchschnitt(1,5,3,4,7,2) = 3,666666666666
3. listeAusgaben(dieListe): Gibt die Liste zeilenweise auf der Konsole aus. Der jeweilige Index in der Liste wird vor dem Element ausgegeben.\
Beispiel: listeAusgeben([“Hallo”,”Welt”,5,10,2]) gibt folgendes aus:
    > 0 Hallo\
    1 Welt\
    2 5\
    3 10\
    4 2

4. maximum(dieListe): Gibt die größte Zahl der übergebenen Liste zurück. Die Funktion max darfst du natürlich nicht benutzen.
5. swap(dieListe): Tauscht das erste und letzte Element der übergebenen Liste. Es gibt keine Rückgabe, die Liste wird direkt bearbeitet.
6. setzeElemente(dasDict:dict,**neueWerte): Überschreibt/Erstellt mehrere Elemente des übergebenen Dictionaries.\
Beispielcode:
    ```py
    test = {“Hallo”:”Welt”, ”test”:”test”}
    setzeElemente(test, Hallo=15, DerKey=”DerTest”)
    print(test) # Gibt {“Hallo”:15, ”test”:”test”, ”DerKey”:”DerTest”} aus.
    ```


7. Schreibe die Funktion `splitTwice(derString:str, char1:str, char2:str)`. 
Diese wendet die Funktion Split zwei Mal auf `derString` an, erst mit `char1`, dann mit `char2`.\
Beim ersten Split wird eine Liste erstellt, beim zweiten Split werden die einzelnen Elemente bei char2 gesplittet.\
Beispiel: `splitTwice(“Hallo Welt|Das ist ein Test|Granatapfel”, ”|”, ” “)`\
gibt folgende Liste zurück: `[[“Hallo”,”Welt”] , [“Das”,”ist”,”ein”,”Test”] , [“Granatapfel”]]`



## Übung 9.2

Die Teilaufgaben sind unabhängig voneinander lösbar.
Kopiere folgende Zeilen in ein neues Skript:
```py
def dieFunktion(a:int)->int:
	pass

# Unter dieser Zeile nichts verändern!!!
x = [1, 5, 3, -41, -7, 5, 0, -4, 89, -2, 1234, 3, 0, 6, -4, 1, -2, 5, 10, -25, 103]
print(list(map(dieFunktion,x))) # Für dich als Hilfe
x.sort(key=dieFunktion)
print(x)
```

Veränder das Skript so, dass die Sortierungen wie beschrieben durchgeführt werden.\
**Natürlich darfst du nur Code über dem Kommentar bearbeiten.**\
Tipp: Anstatt die Funktion nach jeder Teilaufgabe zu löschen, benenn sie einfach um.

1. Die Liste wird nach Betrag, also vorzeichenlos sortiert. -5 kommt also nach 3.\
Tipp: Nutze die Funktion abs. abs(-5) = 5, abs(5) = 5.
2. Die Liste wird normal sortiert, so wie mit x.sort().
3. Die Liste wird in umgekehrter Reihenfolge nach Größe sortiert (also wie in 2., nur umgekehrt).
4. Die Liste wird normal sortiert (wie in 2.), allerdings soll jede 0 nach ganz hinten verschoben werden. (Soll nur für dieses eine x gelöst werden, nicht universell anwendbar)
5. Die Liste wird nach dem Abstand zur 5 sortiert. 6 ist vor 3, da der Abstand von 6 zu 5 kleiner ist als der Abstand von 3 zu 5.
6. Die Liste wird nach der Anzahl der Zeichen sortiert. Das Minuszeichen gilt dabei als Zeichen: 1 hat ein Zeichen, 10 hat 2 Zeichen, -41 hat 3 Zeichen, 103 hat 3 Zeichen.
7. Die Liste wird nicht sortiert, sondern umgekehrt.




## Übung 9.3

Wie ist die Ausgabe, wenn folgende Codeausschnitte ausgeführt werden würden?\
Es kann auch sein, dass ein Fehler ausgelöst wird.
#### **Schreibe den Code NICHT ab und führe ihn nicht aus! Nur angucken und nachdenken!**


1. 
    ```py
    zahl = 15
    
    def fkt1(x):
        zahl = x
    
    fkt1(5)
    fkt1(10)
    
    print(zahl)
    ```

2. 
    ```py
    zahl = 15
    
    def fkt1(x):
        zahl = x
    
    zahl = fkt1(5)
    
    print(zahl)
    ```

3. 
    ```py
    def fkt1(x):
        return 15
    
    def fkt2(x):
        return fkt1
    
    zahl = fkt2()()
    
    print(zahl)
    ```

4. 
    ```py
    def fkt1(x):
        def fkt2(y):
            return [x] + [y]
        return fkt2
    
    zahl = fkt1(5)(15)
    
    print(zahl)
    ```


## Übung 9.4

Lade dir `Materialien/Heuhaufen.py` runter.

In dieser Aufgabe suchen wir die sprichwörtliche Nadel im Heuhaufen.\
Das heruntergeladene Skript erzeugt eine Liste, welche zufällig viele Elemente enthält. Jedes Element ist entweder “Heu”, “Nadel”, oder eine weitere Liste.\
“Nadel” ist nur ein einziges Mal in der gesamten Struktur enthalten.

Deine Aufgabe ist es, anzugeben, wo das Element “Nadel” zu finden ist.
Das korrekte Ergebnis wird bei jedem Durchlauf direkt am Anfang auf der Konsole ausgegeben.

Oben im Skript gibt es die Möglichkeit, den erzeugten Heuhaufen zu konfigurieren.
Löse die Aufgabe zunächst mit der einfachen Konfiguration:

```py
# r.seed(0) # Einfügen, um stets den selben Heuhaufen zu erhalten

maxTiefe = 2    # Die maximale Tiefe
einheitlicheTiefe = True # Ob die Tiefe zufällig ist
maxStrangeProKnoten = 10 # Wie viele Unterknoten jeder Knoten haben soll
heuhaufenPrinten = True # Ob der Heuhaufen auf die Konsole ausgegeben werden soll
```

Dazu brauchst du keine Rekursion, kannst du aber gerne trotzdem nutzen.

Hast du das geschafft, löse die Aufgabe mit schwieriger Konfiguration:

```py
# r.seed(0) # Einfügen, um stets den selben Heuhaufen zu erhalten

maxTiefe = 4    # Die maximale Tiefe
einheitlicheTiefe = False # Ob die Tiefe zufällig ist
maxStrangeProKnoten = 7 # Wie viele Unterknoten jeder Knoten haben soll
heuhaufenPrinten = True # Ob der Heuhaufen auf die Konsole ausgegeben werden soll
```







