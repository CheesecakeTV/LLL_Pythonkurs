
## Zusatzübung 17: Benutzeroberflächen, Threading

Wer beim schreiben besonders klug wirken will, schlägt gerne mal die Bedeutung
einzelner Wörter auf duden.de nach.
In dieser Zusatzübung programmieren wir ein Tool, was dies erleichtern soll.

Halte dich beim programmieren an den unten stehenden Ablauf, dann hast du es deutlich einfacher.

Der Aufbau der Benutzeroberfläche soll ungefähr so sein:\
Ein größerer Text oben für das Wort des Tages.\
Darunter ein Input-Feld als Suchleiste.\
(Optional) Darunter eine Tabelle, um die Suchergebnisse aufzulisten.\
Unten ein größeres Multiline, um die Definition des ausgewählten Suchergebnis auszugeben.

Um es dir etwas einfacher zu machen, orientiere dich an diesem Ablauf:
1. Installiere die Bibliothek `duden`. 
2. Probiere in einem anderen Skript rum, wie man mit der Bibliothek das Wort des Tages abruft
und dessen Definition ausliest.
Das ist nicht ganz so einfach wie es klingt. 
Melde dich also bitte, wenn du es nach 10-15 Minuten noch nicht herausgefunden hast.
3. Erstelle das Layout der Benutzeroberfläche.
4. Beim Starten des Programms soll das Wort des Tages abgerufen und mit Definition im Layout
angezeigt werden.
5. Das Programm startet dadurch vermutlich recht langsam.
Lass die Abfrage also lieber auf einem eigenen Thread laufen.

Der folgende Teil ist minimal schwieriger, aber ähnlich.
Fang ihn also erst an, wenn du bis hier hin alles geschafft hast.

6. Probiere in einem anderen Skript, wie man mit der `duden`-Bibliothek einzelne Wörter sucht
und an deren Definition rankommt.
**Dabei ist es wichtig, dass auch ähnliche Wörter in den Suchergebnissen enthalten sind.**
7. Wird der in der Suchleiste eingegebene Begriff **verändert**, soll der Begriff im Duden
recherchiert werden. Um es einfach zu halten, nutze nur das erste Suchergebnis.
Gib das Ergebnis testweise auf der Konsole aus.
Beachte, dass das Programm nicht abstürzen soll, wenn kein Ergebnis gefunden wurde.
8. Es soll auf einem anderen Thread gesucht werden.
9. Ist die Suche abgeschlossen, wird das Wort und die Definition im Multiline ausgegeben.

Zusätzliche Teile, um auch für die Schnellen unter euch eine Herausforderung zu schaffen:
10. Alle gefundenen Ergebnisse werden in der Tabelle gelistet.
Das erste Ergebnis wird wie gehabt sofort auf dem Multiline ausgegeben.
11. Wird ein Ergebnis in der Tabelle angeklickt, soll dessen Definition in dem Multiline
ausgegeben werden. Dabei ist es sinnvoll, die Ausgabe in eine eigene Funktion zu verlegen,
damit kein Code kopiert werden muss.
12. Gibt der Nutzer was Anderes ein, wird die Tabelle aktualisiert, sodass die Auswahl
gelöscht wird. Das ist suboptimal.
Stattdessen soll automatisch das erste Element ausgewählt werden.
Das wurde nicht im Kurs behandelt, also viel Spaß bei der Recherche!



