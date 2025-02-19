
x1 = 5
x2 = 10
x3 = 15

x = [5, 10, 15, 0, 10, -5]
y = [1,2,3,4,5,6]

print(x)
print(x[0])
print(x[1])
print(x[-1]) # Letztes Element ausgeben
print(x[1:4]) # Von 1 bis 3 ausgeben
print(x[1:]) # Von 1 bis Ende
print(x[:4]) # Von vorne bis 3
print(x[1:4:2]) # ..Schrittweite 2
print(x[::2]) # ..Schrittweite 2
print(x[::-1]) # Liste Rückwärts

print(x + y)
print(x + x + y)
print(2 * x)

x = [5, 10, 15, 0, 10, -5]
y = [1,2,3,4,5,6]

x[0] = 15
print(x)
del x[2] # Element 2 entfernen
print(x)
