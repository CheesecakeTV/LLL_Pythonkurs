

class SchlechterProgrammiererError(Exception):
    ...

def schlechterProgrammierer():
    raise SchlechterProgrammiererError("Bitte mehr üben")

try:
    schlechterProgrammierer()
except SchlechterProgrammiererError:
    pass


