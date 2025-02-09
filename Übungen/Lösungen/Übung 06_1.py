
eingabe = "Hallo ich Programmiere PYTHON"   # eingabe = input()

# 1. mit Optional
#while "  " in eingabe:
#    eingabe = eingabe.replace("  "," ")

#ausgabe = ""
# for i in eingabe:
#     if i.strip() and i == i.upper(): # Wenn i ein Großbuchstabe ist
#         print(i.lower(),end="")
#         #ausgabe = ausgabe + i
#     else:
#         print(i.upper(),end="")

#print(ausgabe)

# 4.
grossbuchstaben = []
for i in eingabe:
    if i.strip() and i == i.upper(): # Wenn i ein Großbuchstabe ist
        grossbuchstaben.append(i)

grossbuchstaben = grossbuchstaben[::-1]

for i in eingabe:
    if i.strip() and i == i.upper(): # Wenn i ein Großbuchstabe ist
        print(grossbuchstaben[0],end="")
        del grossbuchstaben[0]
    else:
        print(i,end="")

