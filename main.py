import PySimpleGUI as sg
import views
import automata.sentence_interpreter as senInt

sg.theme('DarkBlue')   # Add a touch of color

# All the stuff inside your window.
menu_def = [['Programa', ['Novo', 'Abrir', 'Salvar']],
            ['Conectar'],
            ['Compilar'],
            ['Executar'],
            ['Parar'],
            ['Ajuda', ['Sobre...']],
            ['Sair']
            ]

#Layout columns
input_col = sg.Column([
    [sg.Text('Entradas:')],
    [sg.Text("I1:"), sg.Text('X')],
    [sg.Text("I2:"), sg.Text('X')],
    [sg.Text("I3:"), sg.Text('X')],
    [sg.Text("I4:"), sg.Text('X')],
    [sg.Text("I5:"), sg.Text('X')],
    [sg.Text("I6:"), sg.Text('X')],
    [sg.Text("I7:"), sg.Text('X')],
    [sg.Text("I8:"), sg.Text('X')]
])

output_col = sg.Column([
    [sg.Text('Saídas:')],
    [sg.Text("O1:"), sg.Text('X')],
    [sg.Text("O2:"), sg.Text('X')],
    [sg.Text("O3:"), sg.Text('X')],
    [sg.Text("O4:"), sg.Text('X')],
    [sg.Text("O5:"), sg.Text('X')],
    [sg.Text("O6:"), sg.Text('X')],
    [sg.Text("O7:"), sg.Text('X')],
    [sg.Text("O8:"), sg.Text('X')]
])

boolean_col_left = sg.Column([
    [sg.Text('B1:'), sg.Text('X')],
    [sg.Text('B2:'), sg.Text('X')],
    [sg.Text('B3:'), sg.Text('X')],
    [sg.Text('B4:'), sg.Text('X')],
    [sg.Text('B5:'), sg.Text('X')],
    [sg.Text('B6:'), sg.Text('X')],
    [sg.Text('B7:'), sg.Text('X')],
    [sg.Text('B8:'), sg.Text('X')],
])

boolean_col_right = sg.Column([
    [sg.Text('B9:'), sg.Text('X')],
    [sg.Text('B10:'), sg.Text('X')],
    [sg.Text('B11:'), sg.Text('X')],
    [sg.Text('B12:'), sg.Text('X')],
    [sg.Text('B13:'), sg.Text('X')],
    [sg.Text('B14:'), sg.Text('X')],
    [sg.Text('B15:'), sg.Text('X')],
    [sg.Text('B16:'), sg.Text('X')],
])

left_col = sg.Column([
    [sg.Text('Área de Programação')],
    [sg.Multiline('', size=(75), expand_y=True)]
], expand_y=True)

right_col = sg.Column([
    [sg.Text('Informações do CLP')],
    [sg.Text('Conectado: '), sg.Text('X')],
    [input_col, output_col],
    [sg.Text('Mem. Booleanas:')],
    [boolean_col_left, boolean_col_right],
    ], vertical_alignment='top')

layout = [  [sg.Menu(menu_def)],
            [left_col, right_col],
            ]

# Create the Window
window = sg.Window('clp-programmer v0.1', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Sair': # if user closes window or clicks cancel
        break
    print(event, values)
    if event == 'Testar':
        print(f'Input: {values[1]}')
        senInt.interpretSentece(values[1])
    elif event == 'Sobre...':
        window.disappear()
        views.authors
        window.reappear()

window.close()
