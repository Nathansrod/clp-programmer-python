import PySimpleGUI as sg

sg.theme('DarkBlue')

layout = [
    [sg.Text('Programador de CLPs, utilizando linguagens de sentenças lógicas com parenteses balanceados.')],
    [sg.Text('Autores: Alexandre Londe, Esdras Santos, Júlia Cordeiro e Nathan Rodrigues')],
    [sg.Button('Voltar')]
]

window = sg.Window('Sobre...', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Voltar': # if user closes window or clicks cancel
        break
    print(event, values)

window.close()