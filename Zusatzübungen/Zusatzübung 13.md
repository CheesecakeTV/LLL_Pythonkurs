
## Zusatzübung 13: Benutzeroberflächen

In dieser Übung programmieren wir das Spiel "vier gewinnt".
Wer nicht weiß wie dieses Spiel funktioniert, bitte einmal nachlesen.

![img.png](img/VierGewinnt.png)

Ziel ist es, eine Benutzeroberfläche zu erstellen, über welche 2 Spieler das Spiel spielen können.
Dabei soll automatisch erkannt werden, wenn ein Spieler gewonnen hat.

Orientiere dich an folgendem Ablauf.
Teste deinen Code immer wieder zwischendurch, das erleichtert die ganze Sache immens.
1. Erstelle eine Doppelliste, welche die gleiche Größe hat wie das Spielfeld (7 Zeilen, 6 Spalten).
   1. Sollten eher die Zeilen, oder eher die Spalten die "innere Liste" sein?
   2. Alle Felder werden mit 0 initialisiert. Später bedeutet -1, "gelb" und 1 "rot", 0, dass das Feld frei ist.
2. Schreibe die Funktion `einwurf(farbe:int,spalte:int) -> bool`.
Diese bearbeitet das Spielfeld so, als ob ein Spieler die jeweilige Farbe in die jeweilige Spalte geworfen hätte.
Zurügegeben wird, ob die Aktion erfolgreich war.
Nicht erfolgreich ist sie, wenn die Spalte bereits voll ist.
3. Schreibe die Funktion `testeZeileAufSieg(dieZeile:list[int]) -> int`.
Dieser wird eine Zeile übergeben, also eine (einfach-)Liste.
Hat eine Farbe 4 Steine in Folge in dieser Zeile, wird die jeweilige Farbe zurückgegeben (-1 für gelb und 1 für rot).
Falls nicht, wird 0 zurückgegeben.
4. Schreibe die Funktion `hatJemandGewonnen() -> int`.
Diese Funktion testet alle Zeilen, Spalten und Diagonalen nach einem Sieger.\
Tipp: Untersuche, was `list(zip(*doppelliste))` aus der eingesetzten Doppelliste macht.\
Lass die Diagonalen gerne erstmal weg, wenn du möchtest. Am besten kümmerst du dich erst nachher darum.
5. Erstelle jetzt die Benutzeroberfläche.\
Wichtig: Überlege dir eine vernünftige Art, die Keys der Elemente zu setzen.
Keys können nicht nur Strings sein, sondern fast alles (z.B. Tuples, Funktionen, etc).\
Jedes Feld soll durch einen `sg.Button` dargestellt werden.
Außerdem soll es über dem "Spielfeld" eine Reihe Knöpfe geben, über welche sich nachher die "Steine" einwerfen lassen sollen.
Füge noch ein `sg.Text` zur Anzeige des Siegers und einen `sg.Button` zum neustarten des Spiels hinzu.
Füge eine möglichkeit hinzu anzuzeigen, welcher Spieler aktuell am Zug ist.
6. Erweitere die Funktion `einwurf` so, dass das jetzt belegte Feld auf die entsprechende Farbe gesetzt wird.
Verknüpfe diese Funktion auf eine intelligente Weise mit den Knöpfen zum Einwurf.
7. Ist der Einwurf erfolgreich, soll der andere Spieler am Zug sein.
8. Nach dem Einwurf soll getestet werden, ob ein Spieler gewonnen hat. 
Falls ja, werden sinnvolle Aktionen durchgeführt.
9. Beim Neustart des Spiels soll das Spielfeld geleert werden. 
10. Verschönere das Spiel nach Lust und Laune. Sei kreativ!\
Du könntest zum Beispiel `einwurf` so verändern, dass die "Spielsteine" langsam durch alle Felder fallen, bevor sie liegen bleiben.






