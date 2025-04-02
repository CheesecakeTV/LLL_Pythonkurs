import FreeSimpleGUI as sg

#sg.preview_all_look_and_feel_themes()

sg.theme("DarkGray11")


layout = [
    [
        sg.Text("Hallo Welt"),
        sg.VerticalSeparator(),
        sg.Button("Schrift",key="Beschriftung"),
    ],[
        sg.Button("Weiterer Knopf"),
    ],[
        sg.Input(key="Input",enable_events=True),
    ],[
        sg.HorizontalSeparator(),
    ],[
        sg.Checkbox("Text",key="Checkbox",enable_events=True),
    ],[
        sg.T(key="TextVerändern"),
    ],
]

w = sg.Window("Discord Test",layout)

while True:
    e,v = w.read()
    print(e,v)

    if e is None:
        w.close()
        break

    if e == "Input":
        w["TextVerändern"](
            v["Input"]
        )
        w["Checkbox"](True)

    if e == "Beschriftung":
        print("Hallo Welt")











