import FreeSimpleGUI as sg

sg.set_options(font="Any 14")

size = (5,0)
col1 = sg.Column([
    [
        sg.T("Name:",size=size),
        sg.In(key="Name"),
    ],
    [
        sg.T("Alter:",size=size),
        sg.In(key="Alter"),
    ],[
        sg.Button("Knopf!",key="Knopf",expand_x=True)
    ]
],vertical_alignment="top")

tab1 = sg.Tab("links",[
    [
        col1,
        sg.Multiline(size=(50, 5))
    ]
])

tab2 = sg.Tab("rechts",[[sg.T("Hallo Welt")]])

layout = [
    [
        sg.TabGroup([[tab1,tab2]])
    ],[
        sg.Button("Speichern",key="Speichern")
    ]
]

w = sg.Window("Einheit 17",layout=layout,finalize=True,element_justification="top")
w.read(timeout=1)


while True:

    e,v = w.read()
    print(e)

    if e is None:
        w.close()
        break


