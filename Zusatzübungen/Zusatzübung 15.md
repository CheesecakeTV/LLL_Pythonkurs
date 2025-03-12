
## Zusatuübung 15: OOP, Dunder-Methoden

In dieser Übung programmieren wir etwas nach, was ich fast genauso in einem tatsächlichen
Programm implementiert habe.

Dabei handelt es sich um die Klasse `JsonFile`.
Diese Klasse soll ähnlich funktionieren wie ein dictionary, allerdings werden die enthaltenen
Daten in einer Datei gespeichert.

Tipp: Attribute (und Methoden) einer Klasse, welche mit Unterstrich beginnen, gelten als
"privat" und werden von PyCharm nur innerhalb der Klasse vorgeschlagen.
Laut Konvention dürfen diese Attribute nicht von außerhalb der Klasse aufgerufen werden,
aber zwingen tut Python einen nicht.

Im Folgenden darfst du gerne auch eigene Attribute der Klasse definieren, es wird nicht alles
in den Aufgabenstellungen "vorgekaut". Sei kreativ.

1. Importiere die Module `json` und `os`.
2. Erstelle die Klasse `JsonFile`.
Dieser soll beim initialisieren der zugehörige Dateipfad (str) übergeben werden.
3. Definiere die nötigen Methoden, damit Objekte der Klasse beschrieben und ausgelesen werden
können wie normale Dictionaries:
    ```py
    x = JsonFile("test.json")
    x["Hallo"] = "Welt"
    print(x["Hallo"])
    ```
   1. Soll ein Key gelesen werden der nicht enthalten ist, wird ein `KeyError` ausgelöst.
4. Definiere die Methode `__str__`, sodass Json-Files vernünftig auf der Konsole ausgegeben werden können.
5. Definiere die Methode `_save() -> None`.
Diese soll alle im Objekt abgelegten Daten im JSON-Format in den übergebenen Dateipfad speichern.
6. Definiere die Methode `_read() -> bool`.
Diese soll die im Dateipfad gespeicherten Daten auslesen und im Objekt ablegen.
Wird die Datei erfolgreich ausgelesen, wird `True` zurückgegeben, sonst `False`.
7. Nach dem Überschreiben eines Keys (siehe 3.) soll automatisch die zugehörige Datei
aktualisiert werden.
   1. Aus Leistungsgründen soll die Datei nur dann aktualisiert werden, wenn sich der Wert
   auch geändert hat.
8. Beim Erstellen der Instanz soll die Datei, falls vorhanden, automatisch ausgelesen werden.
9. Beim ersten Erstellen der Datei soll der Key `_erstelltVon` mit abgespeichert werden.
Beim normalen Speichern soll der Key `_geändertVon` mit abgespeichert werden.
Diese Keys enthalten jeweils den Anmeldenamen des Windows-Nutzers, welchen du mit `os.getlogin()`
auslesen kannst.

Erstelle die Klasse `Ordner`.

10. Dieser wird ein Ordnerpfad übergeben, welcher mit einem Schrägstrich `/` endet, z.B.: `test/`.
11. Beim Initialisieren mit der Klasse soll der entsprechende Ordner erstellt werden.
Nutze dafür `os.mkdir(ordnerpfad)`.
Wichtig: Teste was passiert, wenn du einen bestehenden Ordner "erstellst".
12. Jeder Ordner hat eine `JsonFile` namens `_vars.json`.
Beim erstmaligen Erstellen dieser Datei wird der Key `nächsterName` auf `0` gesetzt.
13. Definiere die Methode (Alle in der Klasse `Ordner`) `__call__`.
Diese soll eine neue `JsonFile` zurückgeben, welche in dem Ordner angelegt wird.
Der Name dieser Datei ist der Key `nächsterName` der Json-File `_vars.json`.
Nachdem die Datei erstellt wurde, wird `nächsterName` um `1` erhöht.
14. Definiere die Methode `getAlle() -> list[JsonFile]`.
Diese gibt eine Liste mit allen vorhandenen Json-Files im entsprechenden Ordner zurück.
Tipp: `os.listdir()` ist hier hilfreich.



