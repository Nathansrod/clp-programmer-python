import PySimpleGUI as sg

def errorWindow(title, message):
    sg.theme('DarkBlue')

    layout = [
        [sg.Text(message)],
        [sg.Button('Voltar')]
    ]

    window = sg.Window(title, layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Voltar': # if user closes window or clicks cancel
            break
        print(event, values)

    window.close()