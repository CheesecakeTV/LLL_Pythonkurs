



## Übung 13.1 

1. Schreibe die Funktion istPrim(dieZahl:int)->bool, welche zurückgibt, ob die übergebene Zahl eine Primzahl ist. Die Funktion muss nicht besonders effizient sein, einfach nur grundlegend.
2. Der Nutzer soll die Möglichkeit haben, diese Funktion zu nutzen. Dazu gibt er eine Zahl auf der Konsole ein. Das Programm gibt aus, ob die Zahl eine Primzahl ist.
3. Verlangsame deine Funktion zum Testen um 3 Sekunden, indem du time.sleep(3) nutzt.
4. Werden sehr große Zahlen eingegeben, braucht das Programm recht lange zum berechnen. Deswegen soll der Nutzer die Möglichkeit haben, während der Berechnung bereits die nächsten Zahlen einzugeben.
5. Sorge dafür, dass der Nutzer das Programm nicht zum Absturz bringt, wenn er eine nicht-Zahl eingibt.


## Übung 13.2

Entscheide, welches Objekt zur Synchronisation angewendet werden sollte und warum.\
Folgende Objekte haben wir behandelt:
Lock, Semaphore, Barrier, Event\
Diese können auch mehrfach vorkommen.

1. Du betreibst einen Minecraft-Server.
Um zu verhindern, dass der Server überlastet wird, möchtest du begrenzen, wie viele Nutzer gleichzeitig eine Verbindung haben dürfen.

2. Du berechnest eine physikalische Simulation mithilfe mehrerer Prozesse (Threads).
Die Simulation berechnet für jede Sekunde einen Schritt.
Der nächste Schritt soll jedoch erst berechnet werden, wenn der vorherige Schritt vollständig abgeschlossen ist.

3. Du betreibst eine Datenbank, auf welche verschiedene Threads zugreifen.
Du musst verhindern, dass mehrere Threads gleichzeitig auf die Datenbank schreiben.

4. Du betreibst eine Plattform für Unikurse.
Jeder eingeschriebene Student wird durch eigene Threads "betreut".
Veröffentlicht der Professor eine neue Datei, sollen alle Studenten benachrichtigt werden.

5. Ein Programm hat mehrere Module, welche jeweils auf einem eigenen Thread laufen.
Der Nutzer soll die Module jeweils über eine GUI an- und ausschalten können.
Ist ein Modul ausgeschaltet, macht es nichts, außer auf die Einschaltung zu warten.


## Übung 13.3

Kopiere folgende Funktion in deinen Code:

```py
import time

def printSchlecht(text:str) -> None:
    for i in text:
        print(i,end="")
        time.sleep(0.01)
        print("")
```

Diese Funktion soll den übergebenen Text auf der Konsole ausgeben, tut dies jedoch ziemlich langsam.

1. Starte 5 Threads von `printSchlecht` gleichzeitig mit unterschiedlichen Texten.
Was passiert und wie erklärst du die Ausgabe?
2. Nutze ein Lock um die Funktion `printSchlecht` so zu verändern, dass alle Texte korrekt ausgegeben werden.
Ersetze das Lock beim Initialisieren (erstellen) durch eine `Semaphore(2)`. 
Glücklicherweise sind die Methoden von Lock und Semaphore sehr ähnlich, weswegen du sonst nichts am Code ändern musst.
Was passiert und wie erklärst du die Ausgabe?
3. Nutze eine Barrier, um ganz am Ende des Programms (Wenn alle Threads fertig sind) einmal "Fertig" ausgeben zu lassen.
Du darfst dabei weder `.join()`, noch `.isAlive()`, noch `time.sleep()`, noch `events` nutzen.


## Übung 13.4 

(Tatsächlich ein Programm, welches ich mal geschrieben habe. Sehr nützlich.)

Installiere die Bibliothek `Clipboard`.

1. Informiere dich, wie man mit dieser Bibliothek die aktuelle Zwischenablage ausliest.
2. Erstelle eine Benutzeroberfläche, welche die aktuelle Zwischenablage anzeigt. 
3. Wird neuer Text kopiert, soll sich die Benutzeroberfläche automatisch aktualisieren. 
Timeout ist dabei tabu!
4. Füge der Benutzeroberfläche eine Listbox hinzu. 
In dieser soll der Verlauf angezeigt werden, also welche Texte vorher kopiert wurden.
5. Wird ein Element der Listbox angeklickt, soll der entsprechende Text in die Zwischenablage kopiert werden.
6. Beschränke die Länge des Verlaufs auf 30.


## Übung 13.5 

Du darfst in dieser Übung maximal 6 zusätzliche Prozesse verwenden, also inklusive Hauptprozess 7.

1. Erstelle die Funktion `istPrim(dieZahl:int)->bool`.
Dise gibt `True` zurück, wenn es sich um eine Primzahl handelt. 
Ansonsten wird `False` zurückgegeben.
2. Berechne damit alle Primzahlen bis 100000.
3. Nutze Multiprocessing, um die Berechnung zu beschleunigen.
Beschleunige die Berechnung so gut du kannst. Dazu darfst du alle Mittel (maximal 6 Prozesse) nutzen, solange du keine Bibliotheken außer Multiprocessing nutzt. Sowas wie ne Lösungsdatei zu importieren ist natürlich auch tabu!
4. Importiere den Decorator njit der Bibliothek `numba`: `from numba import njit`.
Nutze ihn, indem du `@njit` in die Zeile vor der Funktion hinzufügst:
```py
@njit
def istPrim(dieZahl:int)->bool:
```


