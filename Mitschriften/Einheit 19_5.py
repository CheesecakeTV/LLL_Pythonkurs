import time
import FreeSimpleGUI as sg
import threading

def dieFkt():
    while True:
        time.sleep(1)
        w.write_event_value("Event","Value")

layout = [
    [
        sg.Button("Hallo",key="Hallo")
    ]
]

w = sg.Window("Test",layout,finalize=True)
threading.Thread(target=dieFkt,daemon=True).start()

while True:
    e,v = w.read()
    print(e,v)

    if e is None:
        w.close()
        break


