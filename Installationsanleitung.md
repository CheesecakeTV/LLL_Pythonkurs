
## Folge dieser Anleitung präzise und Schritt für Schritt, ansonsten wird definitiv etwas falsch installiert werden.

## 1. Python installieren

Diese Anleitung ist für Python Version 3.13.0, aber sollte für andere Versionen genauso funktionieren.

1. Lade dir den neusten Python-Installer herunter: https://www.python.org/downloads/ \
Dafür ist oben auf der Seite ein gelber Knopf mit `Download Python 3.13.0` (Oder einer anderen Version)

2. Hast du es bereits ausgeführt und installiert, weil du dachtest, du müsstest dieser Anleitung nicht genau folgen? Dann deinstallier es wieder und folge der Anleitung ab jetzt Schritt für Schritt.\
Öffne den Installer. Ganz auf der ersten Seite gibt es die Option `Add python.exe to PATH` (Siehe Bild).\
Die musst du auswählen. Danach auf `Customize installation` clicken.
    ![](/img/ErsteSeiteInstaller.png)

3. Lass auf dieser Seite alles so wie es ist und klick auf next.
4. Auf dieser Seite musst du zusätzlich `Install Python 3.13 for all users` auswählen (Siehe Bild). Danach auf "Install" klicken.
![](/img/DritteSeiteInstaller.png)
5. Der Rest ist selbsterklärend.

## 2. Python-Konsole öffnen

Mach das einmal um zu testen, ob du Python korrekt installiert hast.

Im Kurs arbeiten wir zu Beginn mit der Python-Konsole.\
Lässt sich die Konsole nicht öffnen, hast du Python falsch installiert.\
Ich nehme mal an, dass jeder Windows nutzt. Wer Linux nutzt findet es schon selbst raus.\
Von Mac hab ich keine Ahnung.

1. Mache einen Rechtsklick auf das Windows-Logo und wähle `Ausführen` (englisch `Run`) aus.\
Alternativ kannst du auch `Windowstaste + R` drücken.
2. Gib `cmd` ein und drück `Enter` oder `ok`. Jetzt sollte sich die cmd öffnen.
3. Gib in der cmd `python` ein und drück enter. Wenn da sowas steht wie `Der Befehl ... konnte nicht gefunden werden`, 
probier mal `python3`. Wenn da der gleiche Fehler steht, oder sich der Windows-Store öffnet, ist Python nicht korrekt installiert.\
Eigentlich sollte da sowas stehen:
    ```batch
    Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information. 
    ```
4. Du bist jetzt in der Python Konsole, hat also alles geklappt. Du kannst ja mal etwas damit rumprobieren, z.B. indem du `5 + 7 * 2` eingibst.


## 3. Pycharm installieren

Pycharm ist eine sogenannte IDE für Python, also ein Programm, mit dem man Python programmiert.\
Es enthält viele Funktionen, die das Programmieren extrem erleichtern.\
Du darfst natürlich programmieren mit was du möchtest, ich mache aber alles in PyCharm vor.\
Viele nutzen auch VSCode, oder die ganz krassen Hacker Neo-Vim. Es gibt unzählige Optionen.

Pycharm ist kostenlos, wenn man weiß wo man es herunterladen muss. Ist etwas versteckt...

1. Öffne diese Seite: https://www.jetbrains.com/de-de/pycharm/download/?section=windows \
NICHT AUF HERUNTERLADEN KLICKEN, sonst hast du die kostenpflichtige Version.
2. Scrolle auf der Seite nach unten, bis du `PyCharm Community Edition` findest (Schwarzer Hintergrund)
3. Darunter gibt es den Knopf "Herunterladen". Den anklicken, um die korrekte Version herunterzuladen.
4. Öffne den Installer. Lass alles auf auf default, bis du die Option `Add "bin" folder to the PATH` angekommen bist.\ 
Diese Option musst du auswählen.



