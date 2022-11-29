import PySimpleGUI as sg
from views import authors, error, program_help, compile_success, confirm_new
import automata.sentence_interpreter as senInt
import reverse_polish_notation.create_notation as createRpn
import reverse_polish_notation.resolve_notation as resolveRpn

sg.theme('DarkBlue') #Add a touch of color

#All the stuff inside your window.
menu_def = [['Programa', ['Novo', 'Abrir', 'Salvar']],
            ['Comandos', ['Compilar']],
            ['CLP', ['Conectar', 'Executar', 'Parar']],
            ['Ajuda', ['Sobre...', 'Programar']],
            ]

#Layout columns
input_col = sg.Column([
    [sg.Text('Entradas:')],
    [sg.Text("I1:"), sg.Text('0', key='k_i1_state')],
    [sg.Text("I2:"), sg.Text('0', key='k_i2_state')],
    [sg.Text("I3:"), sg.Text('0', key='k_i3_state')],
    [sg.Text("I4:"), sg.Text('0', key='k_i4_state')],
    [sg.Text("I5:"), sg.Text('0', key='k_i5_state')],
    [sg.Text("I6:"), sg.Text('0', key='k_i6_state')],
    [sg.Text("I7:"), sg.Text('0', key='k_i7_state')],
    [sg.Text("I8:"), sg.Text('0', key='k_i8_state')]
])

output_col = sg.Column([
    [sg.Text('Saídas:')],
    [sg.Text("O1:"), sg.Text('0', key='k_o1_state')],
    [sg.Text("O2:"), sg.Text('0', key='k_o2_state')],
    [sg.Text("O3:"), sg.Text('0', key='k_o3_state')],
    [sg.Text("O4:"), sg.Text('0', key='k_o4_state')],
    [sg.Text("O5:"), sg.Text('0', key='k_o5_state')],
    [sg.Text("O6:"), sg.Text('0', key='k_o6_state')],
    [sg.Text("O7:"), sg.Text('0', key='k_o7_state')],
    [sg.Text("O8:"), sg.Text('0', key='k_o8_state')]
])

boolean_col_left = sg.Column([
    [sg.Text('B1:'), sg.Text('0', key='k_b1_state')],
    [sg.Text('B2:'), sg.Text('0', key='k_b2_state')],
    [sg.Text('B3:'), sg.Text('0', key='k_b3_state')],
    [sg.Text('B4:'), sg.Text('0', key='k_b4_state')],
    [sg.Text('B5:'), sg.Text('0', key='k_b5_state')],
    [sg.Text('B6:'), sg.Text('0', key='k_b6_state')],
    [sg.Text('B7:'), sg.Text('0', key='k_b7_state')],
    [sg.Text('B8:'), sg.Text('0', key='k_b8_state')],
])

boolean_col_right = sg.Column([
    [sg.Text('B9:'), sg.Text('0', key='k_b9_state')],
    [sg.Text('B10:'), sg.Text('0', key='k_b10_state')],
    [sg.Text('B11:'), sg.Text('0', key='k_b11_state')],
    [sg.Text('B12:'), sg.Text('0', key='k_b12_state')],
    [sg.Text('B13:'), sg.Text('0', key='k_b13_state')],
    [sg.Text('B14:'), sg.Text('0', key='k_b14_state')],
    [sg.Text('B15:'), sg.Text('0', key='k_b15_state')],
    [sg.Text('B16:'), sg.Text('0', key='k_b16_state')],
])

left_col = sg.Column([
    [sg.Text('Área de Programação')],
    [sg.Multiline('', size=(75), expand_y=True, key='k_input_area')]
], expand_y=True)

right_col = sg.Column([
    [sg.Text('Informações do CLP')],
    [sg.Text('Conectado: '), sg.Text('Não')],
    [input_col, output_col],
    [sg.Text('Mem. Booleanas:')],
    [boolean_col_left, boolean_col_right],
    ], vertical_alignment='top')

#Window Layout
layout = [  [sg.Menu(menu_def)],
            [left_col, right_col]]

#Create the Window
window = sg.Window('clp-programmer v0.1', layout)

#Functions
def compileProgram(program): #Compiles the program. Each individual line is submited to the syntax check
    programLines = program.splitlines()
    errorList = []
    i = 1
    for line in programLines: #Test each progrma line
        res = senInt.interpretSentece(line)
        if(res != 0):
            if(res == 1):
                errorList.append(f'Erro de sintaxe linha {i}')
            if(res == 2):
                errorList.append(f'Erro de rótulo linha {i}')
        i += 1
    
    if(len(errorList) != 0): #Error list is not empty
        error.errorWindow('Erro!', 'Erros de compilação detectado, verifique a ajuda.')
    else:
        compile_success.compileSuccessWindow()

def updateScreenValues(inputs, outputs, bools): #Updates values shown in screen
    i = 0
    while i < 8:
        keyInput = f'k_i{i+1}_state'
        keyOutput = f'k_o{i+1}_state'
        window[keyInput].update(inputs[i])
        window[keyOutput].update(outputs[i])
        i += 1
    
    i = 0
    while i < 16:
        keyBoolean = f'k_b{i+1}_state'
        window[keyBoolean].update(bools[i])
        i += 1

#Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: #if user closes window
        break

    if event == 'Novo':
        if(confirm_new.confirmNewProgram()):
            window['k_input_area'].update('')
    elif event == 'Abrir':
        #TODO código de abrir programa a partir de um .txt
        print('Abrir')
    elif event == 'Salvar':
        #TODO código de salvar programa em .txt
        print('Salvar')
    elif event == 'Compilar':
        program = window['k_input_area'].get()
        if(len(program) == 0):
            error.errorWindow('Erro!','A área de programação está vazia.')
        else:
            compileProgram(program)
    elif event == 'Conectar':
        #TODO código de conectar ao CLP
        print('Conectar')
    elif event == 'Executar':
        #TODO código de iniciar a execução do programa compilado
        print('Executar')
    elif event == 'Parar':
        #TODO código que para a execução do programa compilado
        print('Parar')
    elif event == 'Sobre...':
        window.disappear()
        authors.authorsWindow()
        window.reappear()
    elif event == 'Programar':
        window.disappear()
        program_help.programHelpWindow()
        window.reappear()

window.close()
