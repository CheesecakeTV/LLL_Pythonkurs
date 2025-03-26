from functools import wraps

def log(dieFkt:callable) -> callable:
    @wraps(dieFkt)
    def ruckgabe(*args,**kwargs):
        print(dieFkt.__name__)
        return dieFkt(*args,**kwargs)

    return ruckgabe

@log
def x():
    pass

@log
def y():
    pass

x()
x()
y()