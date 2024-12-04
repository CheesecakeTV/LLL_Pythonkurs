
x = "Hallo\n\tWelt"
print(x)

print("Wert:\t15")
print("Wert2:\t30")

x = "Hallo"
y = x + " " + "Welt"
print(y)
print(x * 5)

print(x.replace("ll"," Hallo "))

print(x.lower())
print(x.upper())
print(x.lower() == "hallo".lower())
print("Soße".casefold())

print("hallo welt".capitalize())

print(list(x))
print(x[0])
print(x[-1])
print(x[:3])

# x[0] = "O" # Geht nicht bei Strings!

x = "Hallo an euch im Discord"
print(x.split(" "))
y = x.split(" ")
print(" ".join(y))

print("Ll".casefold() in x.casefold())

variable = 15
wert = 10
print("Variable:",variable)
print("Wert:",wert)

gesamt = "Variable: " + str(variable) # Nervig!
print(gesamt)

gesamt = f"Variable:\t{variable}\nWert:\t\t{wert}"
print(gesamt)
print(f"{variable=}")
