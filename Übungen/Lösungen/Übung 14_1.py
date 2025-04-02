import FreeSimpleGUI as sg

#sg.theme("DarkGray11")
sg.set_options(font="Any 20")

layout = [
    [
        sg.In(key="In1")
    ],[
        sg.In(key="In2")
    ],[
        sg.HSep(),
    ],[
        sg.In(key="Out",disabled=True,disabled_readonly_background_color="")
    ],[
        sg.Button("+",key="+"),
        sg.Button(" - ", key="-"),
        sg.Button(" * ", key="*"),
        sg.Button(" / ", key="/"),
    ]
]

w = sg.Window("Taschenrechner",layout)

while True:
    e,v = w.read()
    print(e,v)

    try:
        zahl1 = float(v["In1"].replace(",","."))
        zahl2 = float(v["In2"].replace(",","."))
    except (ValueError,ZeroDivisionError):
        w["Out"]("Fehler")
        continue

    if e is None:
        w.close()
        break

    if e == "+":
        w["Out"](zahl1 + zahl2)
        continue

    if e == "-":
        w["Out"](zahl1 - zahl2)
        continue

    if e == "*":
        w["Out"](zahl1 * zahl2)
        continue

    if e == "/":
        w["Out"](zahl1 / zahl2)
        continue

