
## Übung 12.1

Entscheide für die folgende Typen, ob es sich (bei deren Instanzen) um
`Iterable`, `Iterator`, keins von beiden, oder beides handelt.

1. list
2. dict
3. str
4. int
5. range
6. enumerate
7. dict.keys()    # Das ist übrigens wirklich ein eigenständiger Typ, namens dict_keys. Values und Items haben auch einen eigenen Typen.
8. dict.values()

## Übung 12.2

Tipp: Löse die Aufgabenteile, indem du die Lösungen der vorherigen Teile verwendest.

Negative Zahlen werden ignoriert.

1. Schreibe einen Generator, welcher alle Ganzzahlen liefert:
`0, 1, 2, 3, …`
2. Schreibe einen Generator, welcher jede gerade Zahl liefert:
`0, 2, 4, 6, …`
3. Schreibe einen Generator, welcher jede Primzahl liefert:
`3, 5, 7, 11, 13, …`
4. Schreibe einen Generator, welcher alle Ganzzahlen liefert und immer neu startet, sobald eine bereits zurückgegebene Zahl zurückgegeben wird:
`0, 0, 1, 0, 1, 2, 0, 1, 2, 3, 0, …`
5. Schreibe einen Generator, welcher die Summe aller bisherigen Ganzzahlen zurückgibt:
`0, 1, 3, 6, 10, 15, 21, 28, …`
6. Schreibe einen Generator, der das Gleiche macht wie enumerate().
   1. Anders als enumerate soll dein Generator unendlich viele Argumente aufnehmen können, sodass man ihn so benutzen kann: \
   `for n, a, b, c in derGenerator(generator1, generator2, generator3):`
   2. Der Generator soll den Index n so ausgeben, so dass er sich so verwenden lässt:\
     `for n, (a, b, c) in derGenerator(generator1, generator2, generator3):`

## Übung 12.3

Implementiere die Funktion `getFirstElem(derIterator:Iterator,default:any=None) -> any`.
Diese gibt das erste Element des übergebenen Iterators zurück.
Ist der Iterator leer, wird `default` zurückgegeben.














