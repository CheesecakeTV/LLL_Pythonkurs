
y = 20 # Globale Variable

def dieFkt():
    x = 15  # Lokale Variable
    return x + y

def dieFkt2():
    x = 10
    global y
    y = 25




