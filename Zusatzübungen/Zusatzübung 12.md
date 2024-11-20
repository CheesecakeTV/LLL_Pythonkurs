
## Zusatzübung 12: OOP

In dieser Zusatzübung programmieren wir ein einfaches Tool für das Spiel [Werwolf](https://de.wikipedia.org/wiki/Die_Werwölfe_von_Düsterwald_(Spiel)), welches den Spielleiter unterstützen soll.
Durch intelligentes Verwenden von OOP, soll sich das Spiel einfach um zusätzliche Rollen erweitern lassen.

Um es einfach zu halten, teilen wir jeden Spieltag in folgende Abschnitte ein:
- Nacht vor Werwölfen (z.B. Nutte, Seer)
- Werwölfe (Die Werwölfe stimmen ab)
- Nacht nach Werwölfen (z.B. Hexe)
- Tag Abstimmung (die Spieler stimmen ab wer raus fliegt)

Orientiere dich an folgendem Ablauf. 
Es wird nicht alles ins kleinste Detail beschrieben, also überlege dir eine sinnvolle Implementierung.
1. Erstelle die Klasse `Spieler`. Bei der initialisierung wird der Name des Spielers übergeben.
2. Jeder Spieler bekommt in der Init eine eigene ID zugewiesen. 
Die ID wird NICHT übergeben, sie wird automatisch ausgewählt.
Du könntest z.B. eine globale Variable nutzen.
3. Jeder erstellte Spieler soll in der init in einer globalen Liste abgelegt werden.
4. Füge die Zeile `self.rolle = self.__class__.__name__` der init hinzu.
Damit wird `self.rolle` auf den Namen der Klasse gesetzt.
5. Erstelle die Methode `__str__(...) -> str`. Diese gibt ID, Namen und Rolle des Spielers zurück.
6. Erstelle folgende Methoden. Diese werden nur von erbenden Klassen genutzt, also lass sie erstmal leer:
`vorWerwolfe()->None`, `werwolfe()->None`, `nachWerwolfe()->None`
7. Erstelle die Methode `abstimmung()->None`.

Fortsetzung folgt...


