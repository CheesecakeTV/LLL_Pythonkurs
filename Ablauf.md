
### Der Ablauf enthält hauptsächlich Notizen für mich
#### Also bitte nicht wundern, wenn die einzelnen Punkte wenig Inhalt haben

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
- Übung 6.1
- List Comprehension: Einzeilige for-Schleifen zum Erstellen einer Liste
- Unterstrich als Variablenname
- Übungen 6.2
- *Blooket*

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
  - Elemente löschen
- values(), keys() und items()
- in - Operator
- .get()
- .copy()
- Übung 8.1

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
- Umfrage zum Kurs

### Lokale und Globale Variablen

- isinstance()
- Map-Funktion
- Key beim sortieren
- Übungen 9.2, 9.3
- (Rekursion zum Knobeln) Übung 9.4

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

## 11. Klassen und Objektorientierung (OOP)

- Grundlagen (Karton-Analogie)
  - Was bedeutet das self bei jeder Methode?
  - Von “außen” auf Attribute und Methoden zugreifen/erstellen
- `__init__()`
- isInstance()
- Mal wieder veränderbar/nicht-veränderbar
- Übung 11.1
- Vererbung
  - super()
- Übung 11.2, 11.3
- Dunder-Methoden (“Magic”-Methoden)
  - str
  - len
  - add, mul
- Übung 11.4
- dir()
- `self.__dict__` nutzen, um Instanz zu kopieren
- pickle Modul
- Mehrere Funktions-Rückgaben
- Lambda-Funktionen
- Übungen 11.5, 9.4
- Umfrage zum Kurs

## 12. Iterators und Generators (Früher Kapitel 14)

- Grundlegende Idee hinter Generatoren?
- Aufbau von Iteratoren
- iter, next und StopIteration
- Erstes Element aus einem Iterator bekommen
- Einfache Generator mit Funktionen
  - Wie funktionieren zip und enumerate?
- Übung 12.1
- Bibliothek [Itertools](https://docs.python.org/3/library/itertools.html)
  - Hier kommt noch Inhalt dazu...
- Iteratoren aus eigener Klasse
- Generator Comprehension

## 13. Decorators (Neu dazu gekommen)
*Auf Platz 2 der schwierigsten Themen dieses Kurses, aber super nützlich wenn man es kann*

#### Nötiges Vorwissen
- Funktionen als Objekt
- Funktionen als Argument
- Funktionen als Rückgabe
- callable-Typehint
- nonlocal Variablen
- Wiederholung: dir()

#### Decorators allgemein
- Decorators als "normale" Funktion die eine Funktion zurückgibt
  - Decorator-Schreibweise
- Argumente
  - Optionale Argumente
- Übungen 13.1 - 13.3

#### Vorgefertigte Decorator und functools
- staticmethod
- property
  - setter
  - functools.cached_property
- functools.wraps
  - update_wrapper
- functools.cache
  - lru_cache
- functools.total_ordering
- functools.partial (Nicht unbedingt ein decorator, aber vergleichbar)
  - functools.partial_method
- An dieser Stelle wäre eine Zusatzübung bonita, ich denk mir was aus.

## 14. Benutzeroberflächen mit PySimpleGUI

Wir nutzen FreeSimpleGUI, ist aber identisch zu PySimpleGUI

- Grundlegende Struktur von PySimpleGUI
- Grundlegende Elemente
  - Text
  - Input
  - Button
  - Separators
  - Checkbox
  - Elemente auslesen
  - Keys setzen
- Elemente beschreiben
- enableEvents
- Fenster schließen
- Themes
- Übung 12.1
- Listen-Elemente
- List (ist Schrott)
- Table
  - size
  - col_width
  - headings
  - justification
- Übungen 12.2, 12.3
- TKinter Events
  - https://web.archive.org/web/20201111211515id_/https://effbot.org/tkinterbook/tkinter-events-and-bindings.htm#events
- timeout-event
- .update()
  - color, button_color
- Übung 12.4
- sg-Popups
- Columns
- Frames
- vertical_alignment
- element_justification
- TabGroups
- Übung 12.5

[Weitere Tutorials zur Bibliothek](https://docs.pysimplegui.com/en/latest/cookbook/original/)

- Umfrage zum Kurs

## 15. Multithreading/Multiprocessing

*Das schwierigste Thema des Kurses, aber trotzdem sehr nützlich und wichtig*

#### Multithreading
- Warum Multithreading?
  - Beispiel an meinem Inventarsystem
- Unterschied zwischen Multithreading und Multiprocessing
- Numba jit
- Zusätzliche Threads starten
  - daemonic Threads
- Informationen vom einen Thread zum nächsten Transportieren
  - Argumente an den Thread übergeben
  - Globale Variablen
- Übung 13.1

#### Synchronisation
- https://docs.python.org/3/library/threading.html#event-objects
- Warum ist Synchronisation nötig?
- .join()
- Objekte zur Synchronisation
  - Lock
  - Semaphore
  - Barrier
  - Event (Ein-/Ausschalter)
- Timer
  - cancel
- Übungen 13.2, 13.3
- Threads mit PySimpleGUI
- Übung 13.4

#### Multiprocessing
- Was ist anders zum Multithreading?
- Pools
  - map
  - https://docs.python.org/3.11/library/multiprocessing.html#module-multiprocessing.pool
- Übung 13.5


## 16. RegEx

- Wofür RegEx?
- Aufteilung: 1. Einheit nur RegEx, 2. Einheit Kombination mit Python
- Regex steht nicht im Ablauf, dafür hab ich eine Präsentation

## 17. Numpy und Pyplot 

- Liste in Array umwandeln
- Einfache Array-Erstellung
- zeros, ones, full, empty
- _like
- arange, linspace
- astype
- Shape
  - reshape
  - flatten
  - Transponieren
  - Grundlegendes Indexen
- Wiederholung zum normalen Indexen
- Teil eines Arrays ersetzen
  - Gesamtes Array auf eine Zahl setzen
- Übung 16.1
- Rechnen mit Numpy-Arrays
  - sin, cos
- Grundlegende Plots
  - plt.plot
  - plt.scatter
  - Mehrere Linien in ein Fenster
  - Übung 16.2
- Umfrage zum Kurs
- Mehrdimensionale Plots
  - Was sind Skalarfelder?
  - Was sind Vektorfelder?
  - 2d Plots
    - meshgrid
    - pcolor
    - pcolormesh
    - colorbar
    - contour
    - quiver
    - streamplot
- Übung 16.3
- Boolsche Funktionen
  - Indexen nach booleschen Funktionen
  - np.where
  - & und |
  - Übung 16.4, 16.5
- Mathematische Funktionen
  - min, max
  - mean
  - sum
  - log, log10, ln
  - Achsen bei den Funktionen angeben
#### np.Random
- plt.hist
  - bins
- Verteilungen
  - Gleichverteilung (random.random)
  - randint
  - Normalverteilung (random.normal)
  - np.clip
  - random.choice
- Übung 16.7 + 16.8 (Ja, vor 16.6)
#### Datetime
- dt.date und dt.datetime
  - datetime in date umwandeln
  - .day, .month, .year, etc.
  - .now()
  - .replace()
- Rechnen mit Daten
- \- (Minus)
- < > (Vergleiche)
  - Timedelta
- Strings in Daten umwandeln und umgekehrt
  - https://www.geeksforgeeks.org/python-strftime-function/
- Übung 16.6
- Anhängen
  - concatinate
- Plots verschönern
  - Subplots
  - Legend
  - Title
  - xLabel, yLabel
  - xTicks, yTicks



## X. Unsortiertes

### Alles was mir mal eingefallen ist, aber ich nicht weiß wohin damit

Dataklassen
Decorators
staticmethod
exec
hash
Closures

Fernet
Datetime
strsimpy (String matching)
pyautogui

Lambda-Funktionen
filter
keys beim Sortieren
Decorators
Eigene Dateien importieren
Mehrere Rückgabewerte von Funktionen



