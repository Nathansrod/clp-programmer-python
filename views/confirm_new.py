import PySimpleGUI as sg

def confirmNewProgram():
    sg.theme('DarkBlue')
    returnVal = False

    layout = [
        [sg.Text('Criar um novo programa irá apagar o que não foi salvo.')],
        [sg.Column([[sg.Button('Voltar'), sg.Button('Confirmar')]], justification='center')]
    ]

    window = sg.Window('Novo Programa', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Voltar': # if user closes window or clicks cancel
            returnVal = False
            break

        if event == 'Confirmar':
            returnVal = True
            break

    window.close()
    return returnVal
