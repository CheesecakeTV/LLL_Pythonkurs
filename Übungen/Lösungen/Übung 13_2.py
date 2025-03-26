from functools import wraps

def ExceptError(derError:Exception,default:any = None):
    def ExceptError(dieFkt: callable) -> callable:
        @wraps(dieFkt)
        def ruckgabe(*args, **kwargs):
            try:
                return dieFkt(*args, **kwargs)
            except derError:
                return default

        return ruckgabe
    return ExceptError

@ExceptError(ZeroDivisionError,0)
def schlecht():
    1 / 0

print(schlecht())
