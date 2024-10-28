## Übung 3.1

Erstelle 3 Zahlen-Variablen: x,y und z. Die Werte darfst du selbst aussuchen.

Schreibe Bedingungen, welche die folgenden Fälle prüfen und gib deren Ergebnis auf der Konsole aus. 
Versuche dabei so wenig Operatoren (>, <=, and, not, etc…) wie möglich zu verwenden.

1. x ist größer als y.
2. x ist größer als y und kleiner als z.
3. z ist größer oder gleich x + y
4. x plus y ist gleich x mal y
5. x ist größer als y, oder z ist kleiner als y
6. x ist größer als y, oder x ist kleiner als y
7. Entweder ist x größer als y, oder x ist größer als z. Beides darf nicht erfüllt sein.


## Übung 3.2

Der Nutzer gibt eine Ganzzahl ein. 

1. Falls es sich um eine negative Zahl handelt, soll `Bitte nur positive Zahlen eingaben` ausgegeben werden.

2. Das Programm gibt alle Zahlen von 2 bis zur eingegebenen Zahl auf der Konsole aus.\
Wird eine 0 oder 1 eingegeben, gibt das Programm nichts aus.
Beispiel:
    ```
    >> 8
    2
    3
    4
    5
    6
    7
    ```

3. Zu jeder ausgegebenen Zahl gibt das Programm aus, ob die Eingabe durch diese Zahl teilbar ist.
Tipp: `int(zahl) == zahl` ergibt True, wenn die Zahl eine Ganzzahl ist.\
Beispiel:
    ```
    >> 8
    2 Ja
    3 Nein
    4 Ja
    5 Nein
    6 Nein
    7 Nein
    ```

4. Falls es sich um eine Primzahl handelt, soll "Die Zahl ist eine Primzahl" ausgegeben werden.\
(Eine Primzahl ist ausschließlich durch 1 und sich selbst teilbar, also hinter jeder Ausgabe von 3. muss “Nein” stehen)

5. Das Skript soll so lange wiederholt werden, bis der Nutzer nichts eingibt, also einfach so enter drückt.

6.  Handelt es sich nicht um eine Primzahl, wird die größte Zahl, durch welche geteilt werden kann, ausgegeben.\
Beispiel:
`8 -> 4`
`52 -> 26`
`100 -> 50`
`17 -> Primzahl`





