

def gen1():
    n = 0
    while True:
        yield n
        n += 1

def gen2():
    for n in gen1():
        yield n * 2

def gen3():
    yield 2

    temp = gen2()
    next(temp)
    for n in temp:
        n += 1  # alle ungeraden Zahlen

        istPrim = True
        for k in range(3,n):
            if n % k == 0: # if teilbar
                istPrim = False
                break

        if istPrim:
            yield n

def gen4():
    for n in gen1():
        for k in range(n + 1):
            yield k

