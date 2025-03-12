import os
import json

class JsonFile:
    def __init__(self,pfad:str):
        assert pfad # Bonuspunkte, stand nicht in der Aufgabenstellung
        self.pfad = pfad

        self.werte = {  # Wenn die Datei bereits existiert, wird dieser Key sowieso überschrieben
            "_erstelltVon":os.getlogin()
        }
        self._read()

    def __getitem__(self, item):
        return self.werte[item]

    def __setitem__(self, key, value):
        prevVal = self.werte.get(key)

        if prevVal == value:
            return

        self.werte[key] = value
        self._save()

    def __str__(self) -> str:
        return f"<JsonFile {self.pfad} mit {len(list(self.werte.keys()))} Element(en)>"

    def __repr__(self) -> str: # Nicht in Aufgabenstellung
        return self.__str__()

    def _save(self) -> None:
        self.werte["_geändertVon"] = os.getlogin()
        with open(self.pfad,"w") as f:
            f.write(json.dumps(self.werte,indent=4))

    def _read(self) -> bool:
        try:
            with open(self.pfad,"r") as f:
                self.werte = json.loads(f.read())
            return True
        except (FileNotFoundError,json.JSONDecodeError,PermissionError):
            # json.JSONDecodeError wird ausgelöst, wenn json die Datei nicht decodieren kann
            return False

class Ordner:
    def __init__(self,pfad:str):
        assert pfad[-1] == "/"  # Bonuspunkte, stand nicht in der Aufgabenstellung

        self.pfad = pfad

        if pfad.count("/") > 1: # Für die Extrapunkte...
            # Würde ich normalerweise niemals hier einfach so rein schreiben, sondern definitiv in ne eigene Funktion...
            temp = ""
            for name in pfad.split("/")[:-1]:
                try:
                    os.mkdir(temp + name)
                    temp += name + "/"
                except FileExistsError:
                    continue
        else: # So hätte man es für den Standard-Fall lösen können.
            # Das if...else ist hier nicht nötig, ich nutze es nur, um die beiden Lösungen zu zeigen.
            try:
                os.mkdir(pfad)
            except FileExistsError:
                pass

        self.vars = JsonFile(pfad + "_vars.json")
        if not "nächsterName" in self.vars.werte:
            # Hier wäre es sinnvoller, __contains__ in JsonFile zu definieren.
            # Habe ich aber beim erstellen der Übung nicht dran gedacht, also was will man machen...
            # Alternativ könnte man mit try...except prüfen, ob der Key enthalten ist.
            self.vars["nächsterName"] = 0

    def __call__(self) -> JsonFile:
        nachsterName = self.vars["nächsterName"]
        self.vars["nächsterName"] = nachsterName + 1

        return JsonFile(self.pfad + str(nachsterName) + ".json")

    def getAlle(self) -> list[JsonFile]:
        alleDateien = list()
        for name in os.listdir(self.pfad):
            alleDateien.append(JsonFile(self.pfad + name))

        return alleDateien







