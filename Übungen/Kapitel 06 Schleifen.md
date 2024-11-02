
## Übung 6.1

Die Teilaufgaben sind unabhängig voneinander lösbar, also halt dich nicht zu lange daran auf.

1. Der Nutzer gibt einen Satz auf der Konsole ein.
Zurückgegeben wird der gleiche Satz, nur dass jeder Anfangsbuchstabe groß geschrieben wurde.\
Tipp: Sieh dir an, was .capitalize() macht.\
Optional: Verwende nicht .capitalize() (Wow, danke für den Tipp)

    Beispiel:
    > \>> Hallo, ich programmiere Python\
    Hallo, Ich Programmiere Python

2. Doppelte Leerzeichen sollen entfernt werden. \
Rechne damit, dass der Nutzer nie mehr als 2 Leerzeichen hintereinander schreibt.\
Optional: Rechne doch nicht damit, entferne alle mehrfachen Leerzeichen, selbst wenn mehr als 2 hintereinander stehen (Die optionalen Teile sind diesmal sehr kreativ).
Alle Großbuchstaben sollen ausgegeben werden:
    > \>> Hallo ich Programmiere PYTHON\
    HPPYTHON

3.  Alle Großbuchstaben sollen durch Kleinbuchstaben ersetzt werden und andersrum:
    > \>> Hallo ich Programmiere PYTHON\
    hALLO ICH pROGRAMMIERE python

4. Alle Großbuchstaben sollen in umgekehrter Reihenfolge ausgegeben werden. Kleinbuchstaben werden nicht beeinflusst:
    > \>> Hallo ich Programmiere PYTHON\
    Nallo ich Orogrammiere HTYPPH



## Übung 6.2

Die Teilaufgaben sind unabhängig voneinander lösbar.

Kopiere folgenden Codeausschnitt in ein leeres Skript:
```py
y = [1, 6, 4, 4, 3, 1, 2, 6, 4, 4, 7, 2, 3, 8, 4, 3, 6]
x = list(range(len(y)))
```

1. Erkläre, was in der Liste x steht.
2. Erstelle die Liste z. Diese soll jeweils das Doppelte der Zahlen aus y enthalten.
   1. Nutze dazu eine for-Schleife
   2. Nutze eine list-Comprehension
3. Gib die Listen x und y Elementweise aus:

    >y - x\
    1 - 0\
    6 - 1\
    4 - 2\
    4 - 3

    usw…










