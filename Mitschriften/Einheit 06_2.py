import json

x = [1,2,3,4,5,"Hallo","Welt",[6,7,8]]

with open("Struktur.json","w") as f:
    f.write(json.dumps(x,indent=4))

with open("Struktur.json","r") as f:
    geladen = json.loads(f.read())

print(geladen)
