# Veränderbar
x = [1,2,3]
y = x.copy() # .copy() sorgt dafür, dass die Liste tatsächlich kopiert wird, nicht nur die Referenz
print(y)
x[0] = 10
print(y)

# Nicht veränderbar
x = 10
y = x
print(y)
x = 15
print(y)


x = [[1]] * 5
print(x)
x[2] = [5]
print(x)

