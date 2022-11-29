import PySimpleGUI as sg

def saveFileWindow():
    path = ''
    sg.theme('DarkBlue')
    layout = [
        [sg.T("")], 
        [sg.Text("Escolha uma pasta: "), sg.Input(key="k_folderpath" ,change_submits=True), sg.FolderBrowse(button_text="Navegar",key="k_browse")],
        [sg.Text("Nome do arquivo: "), sg.Input(key="k_filename", default_text='program')],
        [sg.Button("Confirmar")]
        ]

    window = sg.Window('Salvar programa', layout, size=(600,150))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Voltar': # if user closes window or clicks cancel
            break
        elif event == 'Confirmar':
            print(values)
            path = values['k_folderpath'] + '/' + values['k_filename']
            break

    window.close()
    return path

def openFileWindow():
    path = ''
    sg.theme('DarkBlue')
    layout = [
        [sg.T("")], 
        [sg.Text("Escolha um arquivo: "), sg.Input(key="k_filepath" ,change_submits=True), sg.FileBrowse(button_text="Navegar",key="k_browse")],
        [sg.Button("Confirmar")]
        ]

    window = sg.Window('Abrir programa', layout, size=(600,150))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Voltar': # if user closes window or clicks cancel
            break
        elif event == 'Confirmar':
            print(values)
            path = values['k_filepath']
            break

    window.close()
    return path