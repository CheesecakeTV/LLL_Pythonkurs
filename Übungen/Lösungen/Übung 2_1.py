
# int -> str
# Allgemein alles (außer Zahl ist länger als 4300 Zeichen)

# float -> str
# Allgemein alles

# str -> int
# Muss sinnvolle Zahl sein, ohne Komma
# Geht nicht: int("5.5")
int("5") # Geht

# str -> float
# Muss sinnvolle Zahl sein
float("5.5") # Funktioniert
# Geht nicht: float("5,5")

# bool
# Wird True:
# Zahlen, die nicht 0 sind
# Nicht-leere Strings
# Leerzeichen zählen als Zeichen


