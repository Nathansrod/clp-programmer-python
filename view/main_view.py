import PySimpleGUI as sg
from authors import authorsView
from automata.sentence_interpreter import interpretSentece

sg.theme('DarkBlue')   # Add a touch of color

# All the stuff inside your window.
menu_def = [['Programa', ['Novo', 'Abrir', 'Salvar']],
            ['Compilar'],
            ['Conectar'],
            ['Executar'],
            ['Parar'],
            ['Ajuda', ['Sobre...']]
            ]
layout = [  [sg.Menu(menu_def)],
            [sg.Text('Tela de Teste Integrando com Autômato')],
            [sg.Text('Sentença:'), sg.InputText()],
            [sg.Button('Testar'), sg.Button('Cancelar')] ]

# Create the Window
window = sg.Window('clp-programmer v0.1', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancelar': # if user closes window or clicks cancel
        break
    print(event, values)
    if event == 'Testar':
        print(f'Input: {values[1]}')
        interpretSentece(values[1])
    elif event == 'Sobre...':
        window.disappear()
        authorsView()
        window.reappear()

window.close()