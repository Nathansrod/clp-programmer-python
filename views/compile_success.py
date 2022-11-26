import PySimpleGUI as sg

def compileSuccessWindow():
    sg.theme('DarkBlue')
    layout = [
        [sg.Text('Compilação concluída com sucesso!')],
        [sg.Button('Ok!')]
    ]

    window = sg.Window('Sucesso!.', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Ok!': # if user closes window or clicks cancel
            break
        print(event, values)

    window.close()
