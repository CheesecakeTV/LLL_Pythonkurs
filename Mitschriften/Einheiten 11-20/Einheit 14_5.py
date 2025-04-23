
class test:

    def __iter__(self):
        return self

    def __next__(self):
        ...

x = (i for i in range(10))

print(next(x))
