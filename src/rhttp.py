import PySimpleGUI as sg
import requests

def run():
    layout = [
        [sg.Text("Endpoint:"), sg.InputText(key="endpoint")],
        [sg.Submit(), sg.Button("Quit")]
    ]

    window = sg.Window("Rose Enhanced Toolkit - HTTP(s)", layout)

    while True:
        event, values = window.read()

        if event == "Submit":
            r = requests.get(values["endpoint"])

            window.close()
            sg.Popup(f"Found endpoint in {r.elapsed} seconds.")

        elif event in (sg.WIN_CLOSED, "Quit"):
            window.close()
            break