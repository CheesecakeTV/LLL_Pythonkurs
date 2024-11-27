
y = [1,2,3]
x = [5,6,*y]
print(*x) # * ignoriert die äußeren Klammern
print(5,6,1,2,3)
print(len(x)) # Anzahl an Elementen in x

x.append(15)
x.append(5)
x.extend([1,2,3])

print(x)
print(len(x))

#x.sort() # x sortieren
print(sorted(x)) # Sortiert ohne die Liste zu verändern
print(x)

print(1 in x)

x = ["Hallo","Welt","Discord","5","hallo"]
x.sort()
print(x)
