
x = 7 < 5
y = 7 > 5

if y:
    # Hier später noch was rein schreiben
    pass # Mache nichts
    ...  # Gleich wie pass

if x: # Wenn x
    print("Hallo")
    print("Hallo Welt")
elif y: # Ansonsten, wenn y
    print("...")
else: # Ansonsten

    print("Hallo Discord")

eingabe = ""

if eingabe: # if bool(eingabe)
    print("Eingabe ist da!")
else:
    print("Eingabe nicht da!")

if not eingabe: # if not bool(eingabe), also wenn nichts "eingegeben wurde"
    print("Eingabe ist leer!")

x = 2
y = 7

if x < y: # Viel zu umständlich
    print("True")
else:
    print("False")

print(x < y) # Lieber so

while x < y: # Solange x < y wiederhole...
    print("Hallo Welt")
    x = x + 1
