import PySimpleGUI as sg

def programHelpWindow():
    sg.theme('DarkBlue')
    layout = [
        [sg.Text('Como programar?')],
        [sg.Text("""
Cada linha do programa deve ser composta de uma sentença lógica com 
paranteses balanceados correatmente, vinculada a uma porta ou memória booleana.
Exemplo: O1 = (!I1 ^ (O2 | B3))
As portas disponíveis são definidas por: O1 até O8.
As entradas são indicadas por: I1 até I8.
Memórias booleanas são indicadas por: B1 a B16.
""")],
        [sg.Button('Voltar')]
    ]

    window = sg.Window('Programar', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Voltar': # if user closes window or clicks cancel
            break
        print(event, values)

    window.close()
