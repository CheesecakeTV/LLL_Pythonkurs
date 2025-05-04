import FreeSimpleGUI as sg
import threading
import clipboard as clp
import time

_lange = 30 # Konstanten gebe ich immer nen Unterstrich vorm Namen
verlauf = []

def clpAuslesen():
    """Thread"""
    global verlauf

    vorher = clp.paste()
    while True:
        jetzt = clp.paste()

        if vorher != jetzt:
            vorher = jetzt
            w.write_event_value("Zwischenablage",jetzt)

            if jetzt in verlauf:
                verlauf.remove(jetzt)

            verlauf = [jetzt] + verlauf

            verlauf = verlauf[:_lange]  # Kürzen, falls nötig

        time.sleep(0.2)

layout = [
    [
        sg.T(key="Aktuell",size=(30,0))
    ],[
        sg.Listbox([],key="Verlauf",expand_x=True,size=(0,10),enable_events=True)
    ]
]

w = sg.Window("Zwischenablage",layout,finalize=True,keep_on_top=True)
threading.Thread(target=clpAuslesen,daemon=True).start()

while True:

    e,v = w.read()

    if e is None:
        w.close()
        break

    if e == "Zwischenablage":
        w["Aktuell"](v["Zwischenablage"])
        w["Verlauf"](verlauf)

    if e == "Verlauf" and v["Verlauf"]: # Die Abfrage ist wichtig, falls der Verlauf noch leer ist
        clp.copy(v["Verlauf"][0])
