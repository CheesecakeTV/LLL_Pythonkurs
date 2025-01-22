import json

with open("IP-Adressen.json","r") as f:
    raw = f.read()
    raw = json.loads(raw)

# 2.
print(raw["Johann Roht"])

# 3.
for val in raw.values():
    ...
    #print(val["IP"])

# 4.
for key in raw.keys():
    if key[0] == "E":
        ...
        #print(key)

# 5.
ergebnisse = {}
for key,val in raw.items():
    if key[0] == "E":
        ergebnisse[key] = val

with open("ergebnis.json","w") as f:
    f.write(json.dumps(ergebnisse,indent=4))

# 6.
anzahlPersonen = 0
for key,val in raw.items():
    if "192" in val["IP"]:
        #print(key)
        anzahlPersonen += 1
print(anzahlPersonen)

