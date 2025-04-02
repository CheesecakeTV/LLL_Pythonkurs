import FreeSimpleGUI as sg

#sg.preview_all_look_and_feel_themes()

sg.theme("DarkGray11")
sg.set_options(font="Any 20")


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
    ],[
        sg.Listbox(["Hallo","Welt","Discord"],size=(10,5),enable_events=True,key="Liste")
    ],[
        sg.Table(
            [
                ["Hallo","Welt"],
                ["Hallo","Discord"],
            ],
            headings=["Begrüßung","Name"],
            auto_size_columns=False,
            col_widths=[15,8],
            justification="left", # left, center, right
            enable_events=True,
            key="Tabelle",
        )
    ]
]

w = sg.Window("Discord Test",layout)

while True:
    e,v = w.read()
    print(e,v)

    if e is None:
        w.close()
        break

    if e == "Tabelle":
        print(w["Tabelle"].Values[v["Tabelle"][0]])

    if e == "Input":
        #w["Liste"](["Neue","Liste"])
        w["Tabelle"]([
            ["Eine","Zeile"]
        ])
        w["TextVerändern"](
            v["Input"]
        )
        w["Checkbox"](True)

    if e == "Beschriftung":
        print("Hallo Welt")











