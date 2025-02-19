
x = {"Hallo":"Welt", 15:"Discord", True:"Test"}
y = {"python":"Kurs",16:4}

# x[32] = 128
# del x["Hallo"]

x.update(y)

print(x)

for key in x.keys():
    ...
    #print(key)

for val in x.values():
    ...
    #print(val)

for key,val in x.items():
    ...
    #print("Key:",key,"Val:",val)

# print("Hallo" in x) # Keys
# print("Hallo" in x.values())
#
# print(x.get("bla",0))

z = x.copy()
print(z)
x["Naps"] = "Rainer"
print(x)
print(z)
