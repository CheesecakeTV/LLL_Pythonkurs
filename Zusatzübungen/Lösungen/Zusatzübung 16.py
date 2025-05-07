import duden
import FreeSimpleGUI as sg
import threading

layout = [
    [
        sg.T(key="WortDesTagesText")
    ],[
        sg.In(key="Suchleiste",expand_x=True,enable_events=True)
    ],[
        sg.Table([],headings=[""],expand_x=True,key="Tabelle",enable_events=True,cols_justification="left")
    ],[
        sg.Multiline(disabled=True,key="Ausgabe",expand_x=True,size=(0,10))
    ]
]

w = sg.Window("Duden",layout,finalize=True)
e,v = w.read(timeout=10)

def getWortDesTages() -> None:
    wortDesTages = duden.get_word_of_the_day()
    w.write_event_value("WortDesTages",
                        "Wort des Tages:\n\n" +
                        wortDesTages.name +
                        "\n\n" +
                        wortDesTages.meaning_overview
                        )

threading.Thread(target=getWortDesTages,daemon=True).start()

neuesWortEvent = threading.Event()
def sucheWort() -> None:
    while True:
        print("Suche")
        neuesWortEvent.wait()
        neuesWortEvent.clear()

        gefunden = duden.search(v["Suchleiste"].strip(),exact=False)

        print("Gefunden:",gefunden)

        if not gefunden:
            w.write_event_value("Gefunden",[])
            continue

        w.write_event_value("Gefunden",gefunden)

def wordOffnen(dasWort):
    if dasWort is None:
        w["Ausgabe"]("")
        return

    bedeutung = dasWort.meaning_overview
    if isinstance(bedeutung,list):
        print(bedeutung)
        bedeutung = "\n\n".join(map(str,bedeutung))
    elif bedeutung is None:
        bedeutung = "-- keine Bedeutung --"

    w["Ausgabe"](
        dasWort.name +
        "\n\n" +
        bedeutung
    )

threading.Thread(target=sucheWort,daemon=True).start()

vorherigeSuche = ""
vorherigeErgebnisse = []

while True:
    e,v = w.read()
    print(e)

    if e is None:
        w.close()
        break

    if e == "WortDesTages":
        w["WortDesTagesText"](v["WortDesTages"])

    if e == "Suchleiste" and not v["Suchleiste"].strip() == vorherigeSuche:
        neuesWortEvent.set()
        vorherigeSuche = v["Suchleiste"].strip()

    if e == "Gefunden":
        vorherigeErgebnisse = v["Gefunden"]
        w["Tabelle"](list(map(lambda a:[a],vorherigeErgebnisse)))
        if vorherigeErgebnisse:
            wordOffnen(vorherigeErgebnisse[0])
            w["Tabelle"].update(select_rows=[0])

    if e == "Tabelle" and v["Tabelle"]:
        wordOffnen(vorherigeErgebnisse[
                       v["Tabelle"][0]
                   ])



