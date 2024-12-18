
x = []
for i in range(10):
    if i % 2 == 0: # Wenn i gerade ist
        x.append(i**2)
    else:
        x.append(0)

print(x)

x = [i**2 for i in range(10)]
x = [i**2 for i in range(10) if i % 2 == 0]
x = [i**2 if i % 2 == 0 else 0 for i in range(10)]
print(x)


