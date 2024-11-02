## Zusatzübung 3: String-Matching

Schreibst du auf Discord ein @, werden dir Personen angezeigt, die du taggen kannst.\
Der Text hinter dem @ gilt als Suchtext. Gibst du also @eri ein, werden dir nur Personen angezeigt die "eri im Nutzer- oder Anzeigenamen haben.\
Das Besondere am Discord Suchalgorithmus ist jedoch, dass Schreibfehler teilweise ausgeglichen werden.\
Gibst du z.B. @eic ein (also das "r" vergessen), wird trotzdem "Eric" vorgeschlagen.

Lade dir den Datensatz `Materialien/Namenliste.txt` herunter.\
Daran kannst du deine Algorithmen testen.

Ziel der Übung ist es, eine einfache Suchmaschine zu erstellen, welche trotz gewisser Ungenauigkeiten das gewünschte Ergebnis findet.

Implementiere für jeden der folgenden Fälle eine eigene Funktion, welche jeweils 2 Argumente (s1 und s2) erhält. Die Funktion gibt dann jeweils zurück, ob eine “Ähnlichkeit” vorliegt. s1 ist der Suchtext und s2 wird durchsucht.\
Der Header einer solchen Funktion sieht also z.B. so aus: `genau(s1:str, s2:str) -> bool`\
Tipp: Einige der Teilaufgaben bauen aufeinander auf. Mach dir nicht mehr Mühe als nötig.

Groß- und Kleinschreibung wird immer ignoriert.

1. `genau`: True, wenn s1 genau mit s2 übereinstimmt.\
`genau(“hallo”,”Hallo Welt”)` gibt False zurück.\
`genau(“hallo welt”, “Hallo Welt”)` gibt True zurück.
2. `normal`: Eine “normale” Suche. True, wenn s1 in s2 enthalten ist.\
`normal("hallo","Hallo Welt")` gibt True zurück.\
`normal("hllo" ,"Hallo Welt")` gibt False zurück.
3. `buchstabeVergessen`: Wie “normal”, allerdings darf ein Buchstabe im Suchstring ausgelassen werden.\
`buchstabeVergessen("hallo","Hallo Welt")` gibt irgendwas (egal ob True oder False) zurück.\
`buchstabeVergessen("hllo" ,"Hallo Welt")` gibt True zurück.
4. `buchstabeZuViel`: Wir “normal”, allerdings darf an irgendeiner Stelle ein Buchstabe zu viel im Suchstring enthalten sein.\
`buchstabeZuViel("hallo","Hallo Welt")` gibt irgendwas zurück.\
`buchstabeZuViel("halo welt" ,"Hallo Welt")` gibt False zurück.\
`buchstabeZuViel("hasllo" ,"Hallo Welt")` gibt True zurück.
5. `buchstabeVertauscht`: Wie “normal”, allerdings darf ein Buchstabe durch einen Anderen ersetzt sein.\
`buchstabeVertauscht("hallo","Hallo Welt")` gibt irgendwas zurück.\
`buchstabeVertauscht("hsllo" ,"Hallo Welt")` gibt True zurück.\
`buchstabeVertauscht("hsllp" ,"Hallo Welt")` gibt False zurück.
6. `buchstabeUmgedreht`: Wie “normal”, allerdings darf ein Buchstabe mit seinem Nachbarn vertauscht sein.\
`buchstabeUmgedreht("hallo","Hallo Welt")` gibt irgendwas zurück.
`buchstabeUmgedreht("hsllo" ,"Hallo Welt")` gibt False zurück.
`buchstabeUmgedreht("halol" ,"Hallo Welt")` gibt True zurück.
`buchstabeUmgedreht("ahllo" ,"Hallo Welt")` gibt True zurück.
7. Schreibe jetzt ein Skript, welches alle Namen mithilfe der implementierten Funktionen durchsucht. Es soll eine Liste ausgegeben werden, welche nach Genauigkeit der Treffer sortiert ist:\
Sehr genau: `genau`\
Danach: `normal`\
Danach: `buchstabeVergessen`, `buchstabeZuViel`, `buchstabeVertauscht` (Alle gleichwertig)\
Ungenau: `buchstabeUmgedreht`

Was du dadurch implementiert hast, ist eine vereinfachte Variante des “Weighted Levenshtein” - Algorithmus.

Es gibt allerdings noch viele andere Algorithmen für solche Anwendungsfälle. \
Mein klarer Favorit ist “Cosine Simmilarity”, also die Kosinus-Ähnlichkeit. Dieser Algorithmus ist sehr kompliziert, aber glücklicherweise müssen wir ihn nicht verstehen, um ihn anzuwenden.

8. Nutze die Bibliothek `strsimpy`, um mittels “Cosine Simmilarity” die Liste zu durchsuchen. Sortiere das Ergebnis nach der Ähnlichkeit (Die Funktion gibt die Ähnlichkeit als float zwischen 0 und 1 zurück).\
Tipp: Der Algorithmus funktioniert nur, wenn s1 und s2 mindestens 2 Zeichen lang sind. Überlege dir eine sinnvolle Alternative, falls dies nicht gegeben ist.

