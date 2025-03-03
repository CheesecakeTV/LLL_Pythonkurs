


## 1. Vorbereitung

- Installationsanleitung ist im Repo
    - Kurz mal durchs Repo blättern
- Vorteile von PyCharm
- Während Nachzügler es installieren, Einleitung in den Kurs geben.
- Auf Fragebogen eingehen
    - Diesmal viele Studenten dabei
- Grober Ablauf des Kurses
    - Fragen stellen im Kurs, gerne mündlich
        - Fachwörter, die ich aus Gewohnheit verwende
    - Fängt einfach an, wird immer komplexer
        - Wichtig, die Grundlagen ernst zu nehmen
    - Dauer des Kurses
    - Allgemeiner und Fortgeschrittener Teil
        - Anwendungen eher im fortgeschrittenen Teil
        - Anmerkungen zu Themen die für Programmierer anderer Sprachen relevant sind
    - Übungen und Zusatzübugen
        - "Am schlechtesten sind die Mittelguten"
        - Einfache und schwierige Teilaufgaben ("Optional")
        - Lesen hilft, nicht überfordern lassen
        - Ziel ist es Können aufzubauen, nicht Python-Akademiker zu werden
- Allgemein Vor- und Nachteile von Python
    - Einfach, aber langsam
        - "Python-Magie"
    - Compiler- vs Interpretersprache
    - Anwendungsfälle von Python
        - Mit dem Inventarsystem angeben


### Python Terminal
- Rechnen mit Variablen
- int deklarieren
- `+ - * / ** //`
- Klammern
- float deklarieren
- Übung 1.1

### Jetzt in PyCharm

- Oberfläche erklären (Ausgabefenster)
- Ein Skript ausführen
- print()
    - Klammern hinter Funktionen
    - Mehrere Argumente
- Strings definieren
- input()
    - input("...")
- Strings definieren
- Übung 1.2

## 2. Variablentypen

- Verschiedene Variablentypen
    - int
    - str
    - float
    - bool
- Typecasting (str in int umwandeln, etc.)
    - type()
        - type(type(...))
- Übung 2.1
- *Stand 06.11.2024 Einheit 1*
- Übung 2.2

## 3. Bedingungen und Verzweigungen

- bool-Variablen/Bedingungen
    - True, False
- Vergleiche
    - ==, !=
    - <, >, <=, >=
    - and, or
    - not
- Übung 3.1

- if-Verzweigung
    - else
    - elif
    - Test, ob Variable einen Wert hat mit bool()
    - pass
    - while-Schleifen
- Übung 3.2
- *Stand 13.11.2024, Einheit 2*

## 4. Listen

- Indexe aufrufen
    - Mehrere Indexe aufrufen
    - Von...bis
    - Schrittweite bei Indexen
- Listen "Addieren"
    - Listen "Multiplizieren"
- del
- Übung 4.1, 4.2
- Umfrage zum Kurs
- .copy() (Wird in der Übung erkundet)
- Element appendieren
    - Häufiger Fehler: Liste an Liste appendieren
    - \* um Liste in Liste einzufügen
- len()
- sort()
    - sorted()
- in-Operator
- Übung 4.3, 4.4
- *Stand 27.11.2024 Einheit 3*

## 5. Strings

- 47 String-Methoden
- str()
- Besondere Zeichen  “\n” und “\t”
- "Rechnen" mit Strings
- replace()
- upper(), lower()
    - casefold()
    - capitalize()
- list()
- len()
- split()
- .join()
- in - Operator bei Strings
- f-Strings
- Übungen 5.1 - 5.3


## 6. Schleifen

- while-Schleifen
- break, continue
- for-Schleifen
- range()
    - Typecasten in eine Liste
- enumerate()
- zip()
- *Stand 04.12.2024, Einheit 4*
- Backslash bei Strings (Beim letzten Mal vergessen)
- Übung 6.1
- List Comprehension: Einzeilige for-Schleifen zum Erstellen einer Liste
- Unterstrich als Variablenname
- *Stand 18.12.2024 Einheit 5*
- Übungen 6.2

## 7. Dateien

- Was sind Dateiendungen?
- Dateien auslesen
    - Pfade bei Unterordnern
    - with open… as f: …
- Übung 7.1
- Ordner erstellen
- JSON Modul

## 8. Dictionaries

- Elemente anhängen
    - .update()
    - Elemente löschen
- values(), keys() und items()
- in - Operator
- .get()
- .copy()
- Übung 8.1
- *Stand 22.01.2025 Einheit 6*

## 9. Funktionen

- Warum Funktionen? Wann sollte eine Funktion verwendet werden?
- Grundlegende Funktionen
- Argumente
    - Optionale Argumente / Standardwerte
    - Unendlich viele Argumente
- \* und ** vor Listen/dicts
- Veränderbare / Nicht-Veränderbare Datentypen
- Tuples vs lists
- Docstrings und Typehints
    - any
    - “oder”
    - list[]
    - dict[int:int]
- Übung 9.1
- *Stand 29.01.2025 Einheit 7*
- Umfrage zum Kurs

### Lokale und Globale Variablen

- Typehints auf Variablen
    - any-Typehint
- Lokale/globale Variablen
- isinstance()
- Map-Funktion
- Filter-Funktion
- Key beim sortieren
- Übungen 9.2, 9.3
- (Rekursion zum Knobeln) Übung 9.4
- *Stand 05.02.2025 Einheit 8*

## 10. Try-Except

- Warum Try-Except?
- Try-Except
    - Fehler-Art herausfinden
    - Warum nicht um gesamtes Skript Try-Except packen?
- Fehler-Obergruppen
    - https://docs.python.org/3/library/exceptions.html#exception-hierarchy
- Exception in Variablen “catchen”
- Übung 10.1
- raise
    - assert (Komma, um Beschreibung anzufügen)
- Übungen 10.2, 10.3
