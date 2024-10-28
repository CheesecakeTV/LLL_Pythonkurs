
## Übung 11.1

Erstelle die Klasse Person.

1. Jede Person soll einen Namen (Voller Name), ein Geburtsjahr und ein Geschlecht haben. Alles soll beim Erstellen der Person definiert werden.
2. Schreibe die Methode `getAlter(jahr:int)->int`. Diese gibt zurück, wie alt die Person im entsprechenden Jahr ist (Einfach nur Jahr minus Geburtsjahr).
3. Bei der Initialisierung soll der übergebene Name nach Vor- und Nachname aufgeteilt und im Objekt gespeichert werden (jeweils eigene Variable/Attribut). Nimm dazu an, dass die Person nur einen Vornamen und einen Nachnamen hat, z.B. “Peter Blümke”. 
4. Schreibe die Methode `print()->None`. Diese gibt die Daten der Person lesbar auf der Konsole aus.
5. Schreibe die Methode heirate(diePerson). Dieser wird ein anderes Person-Objekt übergeben, welches gespeichert wird.\
Beispielaufruf:
    ```py
    personA = Person(“Walter Frei”,1980,”M”)
    personB = Person(“Marie Steinke”,1985,”W”)
    personA.heirate(personB)
    ```
   1. Passe die Methode print() an, sodass der Name des Ehepartners mit ausgegeben wird. Es genügt, wenn Vor- und Nachname ausgegeben werden.
6. Wird eine Person verheiratet, wird die verheiratete Person jeweils bei beiden Partnern eingetragen.
7. Erstelle die globale Variable `allePersonen`, welche alle erstellten Personen enthalten soll. Die Personen sollen nicht manuell eingefügt werden, sondern automatisch beim Erstellen einer Person.


## Übung 11.2

Erstelle die Klasse Auto.

1. Jedes Auto hat einen Modelltyp (str), einen Treibstoffverbrauch (float) und ein Gewicht (float).
2. Wird kein Gewicht festgelegt, wird es als 0 angenommen.
3. Erstelle die Methode print(). Diese gibt Informationen über das Auto in dieser Form auf der Konsole aus:

    >Modelltyp: …\
    Treibstoffverbrauch: … l/100km\
    Gewicht: … kg (Diese Zeile wird nur ausgegeben, wenn ein Gewicht gesetzt ist).

Erstelle die Klasse Elektrofahrzeug, welche von der Klasse Auto erbt.

4. Anstatt in l/100km wird der Treibstoffverbrauch in kWh/100km ausgegeben. Überschreibe dazu `Auto.print()`

Erstelle die Klasse Bagger, welche von der Klasse Auto erbt.

5. Zusätzlich zu den üblichen Parametern, wird das Attribut hubkraft (float) definiert. Die Hubkraft hat die Einheit kg und soll bei der Initialisierung übergeben werden.
6. Passe die Methode print() an, sodass der neue Parameter ebenfalls ausgegeben wird. Kopiere dabei nicht die Methode, sondern finde einen Weg, die Methode der Klasse Auto aufzurufen und die neue Zeile anzuhängen.


## Übung 11.3

Eine Exception ist nichts Anderes als eine Klasse. Eine Exception die von einer anderen Exception erbt, ist eine Unterkategorie dieser Exception: https://docs.python.org/3/library/exceptions.html#exception-hierarchy

Erstelle die Exception “SchlechterProgrammiererError” und löse sie testweise über raise aus.


## Übung 11.4

Hilfreiche Übersicht über Dunder-Methoden: https://www.pythonmorsels.com/every-dunder-method/#cheat-sheet

Erstelle die Klasse Vektor.\
Implementiere folgende Funktionalitäten:

1. Jeder Vektor erhält bei der initialisierung mindestens 1 Element:
    ```py
    v1 = Vektor(2,6,3) # v1, v2 und v3 werden in weiteren Beispielen genutzt
    v2 = Vektor(1,2,3)
    v3 = Vektor(1,2,3,4)
    ```

2. Die Anzahl an übergebenen Elementen wird als “grad” abgespeichert.
    ```py
    v1.grad # = 3
    ```

Implementiere folgende Funktionalitäten.\
Beachte, dass bei den meisten Funktionen ein Vektor-Objekt zurückgegeben werden soll.\
Vektor + Vektor soll also Vektor ergeben.

3. Ein Vektor kann wie eine Liste auf der Konsole ausgegeben werden:
    ```py
    print(v1) # Ausgabe: [2,6,3]
    ```

4. Die Länge eines Vektors ist dessen Grad (siehe b):
    ```py
    len(v1) # = 3
    len(v3) # = 4
    ```

5. Zwei Vektoren können wie normale Zahlen addiert werden. Die einzelnen Stellen werden dabei addiert. Stimmt der Grad der Vektoren nicht überein, wird ein TypeError ausgelöst.
    ```py
    v1 + v2 # = Vektor(3,8,6)
    v1 + v3 # = Fehler (TypeError)
    ```

6. Werden zwei Vektoren multipliziert und ihr Grad stimmt überein, wird das Skalarprodukt gebildet. Stimmt der Grad nicht überein, wird ein TypeError ausgelöst. Dabei werden die Elemente jeweils multipliziert und dann addiert:
    ```py
    v1 * v2 # = 2*1 + 6*2 + 3*3 = 23
    v1 * v3 # = Fehler
    ```

7. Wird ein Vektor mit einem float/int multipliziert, werden die Elemente einzeln Multipliziert:\
`v1 * 5 	# = Vektor(2 * 5, 6 * 5, 3 * 5) = Vektor(10,30,15)`
8. Ein Vektor “hoch 2” gibt das Skalarprodukt mit sich selbst aus:\
`v1 ** 2 	# = v1 * v1 = 49`
   1. Wird eine andere Potenz als 2 übergeben, wird ein ValueError ausgelöst:\
   `v1 ** 3	 # = Fehler`
9. Der Betrag (Absolutwert) eines Vektors ist die Wurzel des Vektors hoch 2. Nutze die Funktion sqrt des Moduls math um die Wurzel zu ziehen:\
`abs(v1) # = math.sqrt(v1 ** 2)`
10. Die Elemente des Vektors lassen sich wie bei einer Liste verändern und ausgeben:
    ```py
    v1[0] 		# = 2
    v1[0] = 5 	# Änderung wird vorgenommen
    v1[0] 		# = 5
    v1[5] 		# = Fehler (Index Error)
    ```

11. Vektoren lassen sich wie listen und dicts mit .copy() kopieren (keine dunder Methode).
12. Zwei Vektoren können miteinander verglichen werden, indem deren Betrag verglichen wird. Hinweis: Auf der Liste der Dunder-Methoden gibt es einen Fehler dabei. Die Methode heißt nicht __rt__, sondern __gt__:
    ```py
    v1 > v2 # True
    v2 > v3 # False
    ```
13. Als bool soll der Vektor True sein, wenn seine Länge (abs) nicht 0 ist:
    ```py
    bool(v1) # True
    bool(Vektor(0,0,0)) # False
    ```

## Übung 11.5
Übung zum Ende der Grundlagen.

Diese Übung geht thematisch quer durch alle Themen. 
Sie fragt Verständnis ab, kein Wissen. Es sind nur Übungen, die in dieser Form noch nicht vorgekommen sind.
Die einzelnen Teile sind unabhängig voneinander lösbar.

1. Kopiere folgenden Codeausschnitt in ein leeres Skript. Passe `dieFunktion` so an, dass jeweils nach dem Abstand zur übergebenen Zahl sortiert wird (Es soll für alle Zahlen funktionieren, nicht nur für die hier genutzten).
```py
def dieFunktion(abstandZu:int):
   pass

# Ab hier nichts ändern!!!
x = [1,65,7,3,4,2,3,6,8,43,4,-2,-10,5,2,-13]
x.sort(key=dieFunktion(5))
print("Abstand zu 5:",x)
x.sort(key=dieFunktion(10))
print("Abstand zu 10:",x)
x.sort(key=dieFunktion(-3))
print("Abstand zu -3:",x)
```

2. Schreibe die Funktion `log(zuLoggen:any,vortext:str=””)`.
Die Funktionsweise lässt sich am Besten durch ein Beispiel zeigen:\
    ```py
    x = log(5) # x wird auf 5 gesetzt und “5” wird auf der Konsole ausgegeben.
    x = 5 # Macht genau das Gleiche, nur ohne Ausgabe.
    ```
    Es ist damit also möglich, Werte auf der Konsole auszugeben, ohne zusätzliche Zeilen hinzuzufügen.
    Wird ein Vortext übergeben, wird dieser vor der Ausgabe ausgegeben.

   1. Erstelle die globale Variable loggen. Ist loggen False, soll die log-Funktion nichts auf der Konsole ausgeben.
3. Schreibe die Funktion `istAhnlich(derText:str, suchtext:str)->bool`. 
Grundlegend gibt sie True zurück, wenn der Suchtext im übergebenen Text enthalten ist. Es ist dabei aber erlaubt, dass ein zusätzlicher Buchstabe im Suchtext enthalten ist. Groß- und Kleinschreibung wird ignoriert.\
Beispiele:
    ```py
    istAhnlich(“Hallo Welt”, “hallo”) # True
    istAhnlich(“Hallo Welt”, “haallo”) # True
    istAhnlich(“Hallo Welt”, “haaallo”) # False (2 Buchstaben zu viel)
    istAhnlich(“Hallo Welt”, “halloo”) # True
    ```






