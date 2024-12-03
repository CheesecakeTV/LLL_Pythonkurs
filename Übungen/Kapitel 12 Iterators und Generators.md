## Übung 14.1

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

