import PySimpleGUI as sg
from views import authors, error, program_help, compile_success, confirm_new, file_controller
import automata.sentence_interpreter as senInt
#from reverse_polish_notation import create_notation, logical_structure
import reverse_polish_notation.create_notation as create_notation
import reverse_polish_notation.logical_structure as logical_structure
import communication as comm

sg.theme('DarkBlue') #Add a touch of color
logicalStructure = logical_structure.LogicalStructure([]) #Creating an empty logicalStructure
inExecution = False
isConnected = False

#All the stuff inside your window.
menu_def = [['Programa', ['Novo', 'Abrir', 'Salvar']],
            ['Comandos', ['Compilar']],
            ['CLP', ['Conectar', 'Executar', 'Parar']],
            ['Ajuda', ['Sobre...', 'Programar']],
            ]

#Layout columns
input_col = sg.Column([
    [sg.Text('Entradas:')],
    [sg.Text("I1:"), sg.Text('False', key='k_i1_state')],
    [sg.Text("I2:"), sg.Text('False', key='k_i2_state')],
    [sg.Text("I3:"), sg.Text('False', key='k_i3_state')],
    [sg.Text("I4:"), sg.Text('False', key='k_i4_state')],
    [sg.Text("I5:"), sg.Text('False', key='k_i5_state')],
    [sg.Text("I6:"), sg.Text('False', key='k_i6_state')],
    [sg.Text("I7:"), sg.Text('False', key='k_i7_state')],
    [sg.Text("I8:"), sg.Text('False', key='k_i8_state')]
])

output_col = sg.Column([
    [sg.Text('Saídas:')],
    [sg.Text("O1:"), sg.Text('False', key='k_o1_state')],
    [sg.Text("O2:"), sg.Text('False', key='k_o2_state')],
    [sg.Text("O3:"), sg.Text('False', key='k_o3_state')],
    [sg.Text("O4:"), sg.Text('False', key='k_o4_state')],
    [sg.Text("O5:"), sg.Text('False', key='k_o5_state')],
    [sg.Text("O6:"), sg.Text('False', key='k_o6_state')],
    [sg.Text("O7:"), sg.Text('False', key='k_o7_state')],
    [sg.Text("O8:"), sg.Text('False', key='k_o8_state')]
])

boolean_col_left = sg.Column([
    [sg.Text('B1:'), sg.Text('False', key='k_b1_state')],
    [sg.Text('B2:'), sg.Text('False', key='k_b2_state')],
    [sg.Text('B3:'), sg.Text('False', key='k_b3_state')],
    [sg.Text('B4:'), sg.Text('False', key='k_b4_state')],
    [sg.Text('B5:'), sg.Text('False', key='k_b5_state')],
    [sg.Text('B6:'), sg.Text('False', key='k_b6_state')],
    [sg.Text('B7:'), sg.Text('False', key='k_b7_state')],
    [sg.Text('B8:'), sg.Text('False', key='k_b8_state')],
])

boolean_col_right = sg.Column([
    [sg.Text('B9:'), sg.Text('False', key='k_b9_state')],
    [sg.Text('B10:'), sg.Text('False', key='k_b10_state')],
    [sg.Text('B11:'), sg.Text('False', key='k_b11_state')],
    [sg.Text('B12:'), sg.Text('False', key='k_b12_state')],
    [sg.Text('B13:'), sg.Text('False', key='k_b13_state')],
    [sg.Text('B14:'), sg.Text('False', key='k_b14_state')],
    [sg.Text('B15:'), sg.Text('False', key='k_b15_state')],
    [sg.Text('B16:'), sg.Text('False', key='k_b16_state')],
])

left_col = sg.Column([
    [sg.Text('Área de Programação')],
    [sg.Multiline('', size=(50), expand_y=True, key='k_input_area')]
], expand_y=True)

right_col = sg.Column([
    [sg.Text('Informações do CLP')],
    [sg.Text('Não Conectado', key='k_conn_text')],
    [sg.Text('Não Executando', key='k_exec_text')],
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
        polishNotations = []
        for line in programLines: #Generate one polish tuple for each line in program
            line = line.replace(' ','')
            line = line.upper()
            newPolish = create_notation.reverse_polish_notation(line)
            identifier = line.split('=')[0]
            polishNotations.append((identifier, newPolish)) #Pushes the tuple into the array

        logicalStructure.updatePolishNotations(polishNotations)
        print(logicalStructure)
        compile_success.compileSuccessWindow()

def executeProgram():
    byte = comm.readButtons()
    string = byte.decode('ascii')
    string = string[1:9]
    print(f'EXEC> {string}')
    if(len(string) == 8):
        stringList = list(string)
        i = 0
        while i < len(stringList):
            if(stringList[i] == '1'):
                stringList[i] = True
            else:
                stringList[i] = False
            i += 1
        logicalStructure.updateInputs(stringList)
        outputList = logicalStructure.updateOutputs()

        responseString = '@'
        for item in outputList:
            if(item == True):
                responseString = responseString + '1'
            else:
                responseString = responseString + '0'
        
        responseString = responseString + '#'
        encodedString = responseString.encode('utf-8')
        comm.sendLedByte(encodedString)
        updateScreenValues(logicalStructure.inputs, logicalStructure.outputs, logicalStructure.booleans)
    

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

def saveProgram():
    path = file_controller.saveFileWindow()
    program = window['k_input_area'].get()
    print(f'Filepath: {path}')
    try:
        file = open(path, 'w')
        file.write(program)
        file.close()
    except:
        error.errorWindow('Erro!','Não foi possivel salvar o arquivo \nno caminho especificado.')

def openProgram():
    path = file_controller.openFileWindow()
    try:
        file = open(path, 'r')
        program = file.read()
        file.close()
        return program
    except:
        error.errorWindow('Erro!', 'Não foi possível abrir o \narquivo especificado.')
        return ''

def setConnected(bool):
    if(bool == True):
        window['k_conn_text'].update('Conectado ao CLP')
        return True
    else:
        window['k_conn_text'].update('Não Conectado')
        return False

def setExecution(bool):
    if(bool == True):
        window['k_exec_text'].update('Em Execução')
        return True
    else:
        window['k_exec_text'].update('Não Executando')
        return False

#Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read(timeout=250) #Awaits 10ms for an event
    if event == sg.WIN_CLOSED: #if user closes window
        break

    #Answering to commands on screen menu
    if event == 'Novo':
        if(confirm_new.confirmNewProgram()):
            window['k_input_area'].update('')
            inExecution = setExecution(False)
    elif event == 'Abrir':
        print('Abrir')
        window.disappear()
        if(confirm_new.confirmNewProgram()):
            program = openProgram()
            window['k_input_area'].update(program)
        window.reappear()
    elif event == 'Salvar':
        print('Salvar')
        window.disappear()
        saveProgram()
        window.reappear()
    elif event == 'Compilar':
        print('Compilar')
        setExecution(False)
        program = window['k_input_area'].get()
        if(len(program) == 0):
            error.errorWindow('Erro!','A área de programação está vazia.')
        else:
            compileProgram(program)
    elif event == 'Conectar':
        print('Conectar')
        if(comm.estabilishConnection() == True):
            isConnected = setConnected(True)
        else:
            isConnected = setConnected(False)
            error.errorWindow('Erro!', 'Não foi possível conectar\nao dispositivo')
    elif event == 'Executar':
        print('Executar')
        if(isConnected):
            inExecution = setExecution(True)
        else:
            error.errorWindow('Erro!', 'Não há dispositivo\nconectado')
    elif event == 'Parar':
        print('Parar')
        logicalStructure.resetStructure()
        comm.sendLedByte(b'@00000000#')
        updateScreenValues(logicalStructure.inputs, logicalStructure.outputs, logicalStructure.booleans)
        inExecution = setExecution(False)
        isConnected = setConnected(False)
    elif event == 'Sobre...':
        window.disappear()
        authors.authorsWindow()
        window.reappear()
    elif event == 'Programar':
        window.disappear()
        program_help.programHelpWindow()
        window.reappear()

    if inExecution:
        executeProgram()

window.close()
