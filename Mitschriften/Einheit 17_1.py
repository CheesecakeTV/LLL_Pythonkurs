import FreeSimpleGUI as sg

sg.set_options(font="Any 14")

layout = [
    [
        sg.Button("Test",key="Test",button_color="red"),
        sg.T("Hallo Welt",font="Any 20")
    ],[
        sg.Input(key="Input",size=(30,3),enable_events=True),
    ],[
        sg.T("Hallo WeltHallo WeltHallo WeltHallo Welt",size=(30,1))
    ],[
        sg.Multiline(key="Multiline",size=(30,10))
    ]
]

w = sg.Window("Einheit 17",layout=layout,finalize=True)
w.read(timeout=1)

w["Input"].bind("<Button-1>","_Knopf")
w["Input"].bind("<Enter>","_Enter")
w["Input"].bind("<Return>","_Eingabe")

while True:

    #e,v = w.read(timeout=1000)
    e,v = w.read()
    print(e)

    if e is None:
        w.close()
        break

    if e == "Test":
        w["Test"].update(button_color = "blue", disabled=True, visible=False)


