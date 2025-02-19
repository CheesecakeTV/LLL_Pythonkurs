
## Übung 10.1

Löse 6 verschiedene Exceptions deiner Wahl aus (natürlich ohne raise).

Hier findest du alle Exceptions: https://docs.python.org/3/library/exceptions.html#exception-hierarchy


## Übung 10.2

1. Schreibe ein Skript, welches den Nutzer so lange zur Eingabe auffordert, bis er eine Ganzzahl (int) eingibt.
2. Nimm 1. und mache daraus die Funktion `inputGanzzahl() -> int`. Die eingegebene Ganzzahl wird von der Funktion zurückgegeben.
3. Optional: Implementiere die Funktion `inputType(derTyp:type) -> any`, welche die gleiche Funktionalität hat wie `inputGanzzahl()`, jedoch mit jedem wandelbaren Datentyp funktionieren soll.\
Beispiel: Wird `inputType(float)` aufgerufen, wird so lange zur Eingabe aufgefordert, bis eine Float eingegeben wird. Die Float wird dann zurückgegeben.
Du darfst dazu keine if-Abfrage nutzen, wir bleiben so abstrakt wie möglich.
   1. Weise den Nutzer darauf hin, was für einen Typen er eingeben soll. Den Namen eines Typens kannst du mit .__name__ als String bekommen.
   `float.__name__` gibt also “float” zurück.


## Übung 10.3

Erstelle die Funktion `meineFkt(dieZahl:int) -> bool`.

Dann implementiere:

1. Wird eine negative Zahl übergeben, wird ein ValueError ausgelöst.
2. Wird kein int (sondern irgendwas Anderes) übergeben, wird ein TypeError ausgelöst.
3. Nutze assert, um auszuschließen, dass eine 0 übergeben wird.
4. Füge allen 3 Fällen eine entsprechende Fehlernachricht hinzu.



