import PySimpleGUI as sg
import ctypes

import rhttp as rhttp

layout = [
    [sg.Text("Welcome to the Rose Enhanced Toolkit!")],
    [sg.Button("HTTP(s)")],
    [sg.Button("Quit")]
]

window = sg.Window("Rose Enhanced Toolkit", layout)

while True:
    try:
        event, values = window.read()

        if event == "HTTP(s)":
            rhttp.run()

        # In the event the user quits
        elif event in (sg.WIN_CLOSED, "Quit"):
            window.close()
            break

    except Exception as e:
        ctypes.windll.user32.MessageBoxW(0, str(e), type(e).__name__, 0)