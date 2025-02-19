
## Übung 5.1

Der Nutzer gibt einen Satz auf der Konsole ein.

1. Das Programm gibt aus, wie viele Wörter der Satz enthält.\
Tipp: Hast du eine Möglichkeit, die Wörter voneinander zu trennen?\
Beispiel:
    ```
    >> Hallo ich programmiere Python
    4
    ```

2. Das Programm gibt den Satz aus, allerdings ein Wort pro Zeile. \
Optional: Verwende keine Schleifen.\
    Beispiel:
    ```
    >> Hallo ich programmiere Python
    Hallo
    ich
    programmiere
    Python
    ```

## Übung 5.2

Der Nutzer gibt irgendeine Zeichenfolge ein.
1. Das Programm gibt im ganzen Satz aus, wie lang die Eingabe ist:
    ```
    >> Hallo Welt
    Die Eingabe hat 10 Zeichen!
    ```
2. Das Programm gibt danach die Zeichenfolge so oft hintereinander aus, dass sie 20 Zeichen lang ist.
Die Zeichenfolge darf am Ende abgeschnitten werden, um genau auf 20 Zeichen kommen zu können.\
Optional: Verwende keine Schleifen. Es gibt eine banal einfache Lösung, aber darauf muss man erstmal kommen...\
Beispiel:
    ```
    >> 12345
    12345123451234512345
    >> Hallo
    Hallo Hallo Hallo Ha
    >> 
    Fehler (Leere Eingabe)
    ```

## Übung 5.3

In dieser Übung erstellen wir einen sehr einfachen (bzw. schlechten) Geheimschrift-Übersetzer.
Dieser erkennt selbst, ob eine Eingabe bereits verschlüsselt ist oder nicht.

Die Verschlüsselung funktioniert so:
Liest man nur jedes 2. Zeichen (beginnend bei 0) des verschlüsselten Wortes, erhält man das Wort.
Liest man nur jedes 2. Zeichen (beginnend bei 1) des verschlüsselten Wortes, erhält man das Wort rückwärts.

Beispiele:
"Hallo" -> "HoallllaoH"
"Welt" -> "WtelletW"

1. Schreibe einen Algorithmus zur Verschlüsselung.\
Optional: Verwende keine Schleifen.
2. Schreibe einen Algorithmus zur Entschlüsselung.
3. Schreibe eine Abfrage, welche testet, ob ein String verschlüsselt ist oder nicht.
4. Kombiniere deine Ergebnisse zu einem Programm, je nach Eingabe entweder verschlüsselt oder entschlüsselt. Es soll so lange wiederholt laufen, bis der Nutzer keine Eingabe mehr tätigt: Eingabe == “”.










