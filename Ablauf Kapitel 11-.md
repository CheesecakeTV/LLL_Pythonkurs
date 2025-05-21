
### Der Ablauf enthält hauptsächlich Notizen für mich
#### Also bitte nicht wundern, wenn die einzelnen Punkte wenig Inhalt haben


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
- *Einheit 11 19.02.2025*
- Übung 11.2, 11.3
- Dunder-Methoden (“Magic”-Methoden)
  - str
  - len
  - add, mul
- *Einheit 12 26.02.2025*
- getitem, setitem
- properties
- Übung 11.4
- dir()
- `self.__dict__` nutzen, um Instanz zu kopieren
- pickle Modul
- Mehrere Funktions-Rückgaben
- Übungen 11.5 (Übersprungen)

## 12. Iterators und Generators (Früher Kapitel 14)

- Grundlegende Idee hinter Generatoren?
- Aufbau von Iteratoren
- iter, next und StopIteration
- Erstes Element aus einem Iterator bekommen
- Einfache Generator mit Funktionen
  - Wie funktionieren zip und enumerate?
- Übung 12.1
- Bibliothek [Itertools](https://docs.python.org/3/library/itertools.html)
  - `count`
  - `accumulate`
  - `chain`
  - `starmap`
  - `tee`
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
- Argumente von Decorators
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
- Übung 14.1
- Listen-Elemente
- List (ist Schrott)
- Table
  - size
  - col_width
  - headings
  - justification
- Übungen 14.2, 14.3
- TKinter Events
  - https://web.archive.org/web/20201111211515id_/https://effbot.org/tkinterbook/tkinter-events-and-bindings.htm#events
- timeout-event
- .update()
  - color, button_color
- Übung 14.4
- sg-Popups
- Columns
- Frames
- vertical_alignment
- element_justification
- TabGroups
- Übung 14.5

[Weitere Tutorials zur Bibliothek](https://docs.pysimplegui.com/en/latest/cookbook/original/)

- Umfrage zum Kurs

## 15. Multithreading/Multiprocessing

*Das schwierigste Thema des Kurses, aber trotzdem wichtig*

#### Multithreading
- Warum Multithreading?
- Unterschied zwischen Multithreading und Multiprocessing
- Numba jit
- Zusätzliche Threads starten
  - daemonic Threads
- Informationen vom einen Thread zum nächsten Transportieren
  - Argumente an den Thread übergeben
  - Globale Variablen
- Übung 15.1

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
- Übungen 15.2, 15.3
- Threads mit PySimpleGUI
- Übung 15.4

#### Multiprocessing
- Was ist anders zum Multithreading?
- Pools
  - map
  - https://docs.python.org/3.11/library/multiprocessing.html#module-multiprocessing.pool
- Übung 15.5
- Manager
- Queue
  - put
  - get
- Pipe
  - send
  - recv
  - send_bytes
  - recv_bytes
  - poll

## 14. (Teil 2) Benutzeroberflächen mit PySimpleGUI

- Multithreading in PySimpleGUI
- Elemente mit target

#### Diverse Praxistipps

- Funktionen als Key
- Tuple als Key
- Eigenes Layout-Element erstellen
- Emojis
- sg.rgb
- fill_form_with_values
- Clipboard
- sg.main()

## 16. RegEx

**Da irgendwie niemand dieses Kapitel leiden kann, wirds übersprungen.**
Ich persönlich finde RegEx super, verstehe aber auch, warum man keinen Bock darauf hat.

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

## 18. Kryptographie

#### Theoretische Grundlagen
- Eigenschaften von Verschlüsselungen und Negativbeispiele
  - Caeser (Substitution)
  - Vigenère (Polyalphabetisch)
  - Skytale (Transposition)
- XOR-Verknüpfungen
  - Warum XOR statt Addition?
  - Vernam-Chiffre
- Ansätze zur Entschlüsselung, Fehler in Verschlüsselungen
  - Häufigkeitsanalyse
    - Häufigkeitsanalyse von 2er-Folgen
  - Enigma (Bekannte Klartextstücke, Rückführung)
  - DVD-Verschlüsselung ("Security-By-Obscurity")
  - Brute-Force
  - Nachdenken (Analytische Lösungen)
  - Quantencomputer
- AES
- Key-Derivation
  - Argon2
- Hashing

#### Praxis
...

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



