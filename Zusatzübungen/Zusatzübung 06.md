## Zusatzübung 6: Grundlagen

Um bei Aldi an der Kasse zu arbeiten, muss man sogenannte PLU Nummern auswendig lernen. 
Das sind Nummern für Artikel, die schlecht zu scannen sind, oder keinen Barcode haben (z.B. Backwaren und Früchte). 
Um so einen Artikel zu kassieren, muss der Kassierer die Nummer wissen und in die Kasse eingeben.

In dieser Übung schreiben wir ein Programm, welches neuen Kassierern dabei hilft, diese Nummern auswendig zu lernen.

Das Programm soll einen Artikel in die Konsole ausgeben, woraufhin der Nutzer 3 Versuche hat, die richtige Nummer einzugeben.

Lade dir die Datei `Materialien/PLU_Nummern.csv` herunter.

Orientiere dich an diesem Ablauf:

1. Untersuche, wie die CSV-Datei aufgebaut ist. Was steht in den einzelnen Zeilen? Was steht in der ersten Zeile?
2. Lade die CSV-Datei in dein Skript. Teile die Daten nach Zeilen auf und lösche die Erste Zeile.
3. Recherchiere, wie die Funktion “randint” der Bibliothek “random” funktioniert und wie man sie nutzt.
4. Nutze die Funktion randint, um eine zufällige Zeile der CSV-Datei auszuwählen. Gib diese Zeile zum Testen auf der Konsole aus.

Implementiere jetzt die eigentliche Abfrage. 
Ich empfehle stark, diese in einem neuen Skript zu schreiben und danach in dein Hauptskript zu übernehmen. 
So ist es einfacher zu testen.

5. Ermittle die Bezeichnung und die PLU-Nummer aus der gewählten Zeile. Gib die Bezeichnung auf der Konsole aus.
6. Implementiere die Abfrage, also dass der Nutzer 3 Versuche hat, die Nummer korrekt einzugeben. Schafft er es nicht, wird die korrekte Nummer mit entsprechender Nachricht ausgegeben.
7. Lass das Skript in Dauerschleife laufen, bis der Nutzer nichts mehr eingibt.
