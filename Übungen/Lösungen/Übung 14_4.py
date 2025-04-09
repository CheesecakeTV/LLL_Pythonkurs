import FreeSimpleGUI as sg

layout = [

]

for zeile in range(10):
    neueZeile = []
    for spalte in range(10):
        neueZeile.append(
            sg.Button(key=f"{zeile}-{spalte}",size=(2,0),button_color="blue")
        )
    layout.append(neueZeile)

w = sg.Window("Knopfmatrix",layout,finalize=True)#,grab_anywhere=True,keep_on_top=True,no_titlebar=True)
# for zeile in range(10):
#     for spalte in range(10):
#         w[f"{zeile}-{spalte}"].bind("<Enter>","_enter")
#         w[f"{zeile}-{spalte}"].bind("<Leave>","_leave")

for zeile in layout:
    for knopf in zeile:
        knopf.bind("<Enter>","_enter")
        knopf.bind("<Leave>","_leave")


while True:
    e,v = w.read()
    print(e)

    if e is None:
        w.close()
        break

    key,event = e.split("_")

    if event == "enter":
        w[key].update(button_color="red")

    if event == "leave":
        w[key].update(button_color="blue")
