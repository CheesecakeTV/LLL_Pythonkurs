
def meinGenerator(max_i):
    i = 0
    while i < max_i:
        yield i
        i += 1

x = meinGenerator(5)
print(next(x))
print(next(x))
print(next(x))

x = meinGenerator(5)
print(next(x))
print(next(x))
print(next(x))



