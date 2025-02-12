
def inputGanzzahl() -> int:
    while True:
        try:
            eingabe = int(input("Bitte gib eine Ganzzahl ein: "))
            return eingabe
        except ValueError:
            print("Falsche Eingabe!")

def inputType(derTyp:type) -> any:
    while True:
        try:
            eingabe = derTyp(input(f"Bitte gib eine {derTyp.__name__} ein: "))
            return eingabe
        except ValueError:
            print("Falsche Eingabe!")

print(inputType(float))
#raise inputType(ValueError)
print("Alles ok")
