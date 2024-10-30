
## Übung 4.1

1. Erstelle die Liste x, welche 10 Zahlen deiner Wahl enthält.\
**Tu im Folgenden so, als ob du die Werte von x nicht kennen würdest.**
2. Gib den 3., 5., und 7. Wert auf der Konsole aus (muss nicht in der gleichen Zeile sein).
3. Ersetze den 3. Wert durch die Zahl 10.
4. Lösche den 4. Wert.
5. Lösche den letzten Wert der Liste.
6. Hänge den Wert 15 an die Liste an.
7. Gib die 5 hintersten Werte auf der Konsole aus.

Führe folgenden Codeabschnitt in einem neuen Skript aus:

```py
x = [1,2,3]
y = x
print(y)
x[0] = 10
print(y)
```
8. Welche Ausgabe hättest du erwartet? Wie deutest du die Ausgabe?
9. Ersetze die 2. Zeile durch `= x.copy()` und führe alles erneut aus.\
Was bewirkt `.copy()` ?


## Übung 4.2

1. Der Nutzer gibt nacheinander einige Ganzzahlen auf der Konsole ein.\
Diese werden in einer Liste gespeichert.\
Gibt der Nutzer nichts ein (""), stoppt die Eingabe und alle eingegebenen Zahlen werden der Reihe nach ausgegeben.

2. Neben der Zahl soll die Summe aller bisherigen Zahlen ausgegeben werden.\
Tipp: Du kannst das Trennzeichen der print-Funktion beeinflussen, indem du das optionale Argument sep veränderst: `print(zahl1, zahl2, sep = “ - “)`.\
Beispiel:
    ```
    1 - 1
    2 - 3
    2 - 5
    10 - 15
    2 - 17
    ```

3. Die Zahlen sollen vor der Ausgabe nach Größe (aufsteigend) sortiert werden. Die Summe wird erst nach dem Sortieren gebildet.

4. Nach der Eingabe soll die größte Eingegebene Zahl aus der Liste gelöscht werden.

5. Die Zahlen sollen nun in umgekehrter Reihenfolge, also von groß nach klein sortiert werden. Denk daran, nur gelernte Wege zu nutzen. Reverse wurde noch nicht gelernt.


## Übung 4.3

Schreibe eine einfache Passwortabfrage:

Der Nutzer soll 3 Versuche haben, eines der richtigen Passwörter einzugeben.
Alle richtigen Passwörter stehen in einer Liste. Denk dir da einfach 3-4 Stück aus.

Wird ein korrektes Passwort eingegeben, gibt das Programm “Zugang erfolgreich” aus.
Werden alle 3 Versuche verbraucht, gibt das Programm “Keine Versuche übrig” aus.
In beiden Fällen wird das Programm beendet.

Tipp: Beende das Programm an einer beliebigen Stelle, indem du exit() verwendest.

1. Implementiere die genannten Funktionalitäten.
2. Zu jedem Passwort soll nun ein Benutzername hinzugefügt werden. Wird eines der Passwörter korrekt eingegeben, wird der Benutzername auf der Konsole ausgegeben.\
Wieder der Hinweis: Wir hatten noch keine Dictionaries, benutze nur das, was wir im Kurs behandelt haben.







