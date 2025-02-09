
# 1.
# gesamt = ""
# for i in range(10001):
#     gesamt = gesamt + str(i) + "\n"

gesamt = "\n".join([str(i) for i in range(10001)])

with open("Zahlen.txt","w") as f:
    f.write(gesamt)

# 2.
primzahlen = []
for i in range(1,1000):
    primzahl = True
    for k in range(2,i):
        if i % k == 0:
            primzahl = False
            break

    if primzahl:
        primzahlen.append(str(i))

with open("Primzahlen.txt","w") as f:
    f.write("\n".join(primzahlen))





