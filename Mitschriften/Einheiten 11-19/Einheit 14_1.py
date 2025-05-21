
x = range(10)

# for i in x:
#     print(i)

y = iter(x)
print(y)

try:
    i = next(y)
    print(i)
    i = next(y)
    print(i)
    i = next(y)
    print(i)
    i = next(y)
    print(i)
    i = next(y)
    print(i)
    i = next(y)
    print(i)
    i = next(y)
    print(i)
    i = next(y)
    print(i)
    i = next(y)
    print(i)
    i = next(y)
    print(i)
    i = next(y)
    print(i)
except StopIteration:
    pass

