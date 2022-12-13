import PySimpleGUI as sg
from zip_creater import make_archive
label1 = sg.Text("Select files to compress")
input1 = sg.Input()
chose_button1 = sg.FilesBrowse("Choose", key="files")
label2 = sg.Text("Select destination folder")
input2 = sg.Input()
chose_button2 = sg.FolderBrowse("Choose", key="folder")
compress_button = sg.Button("Compress")
label3 = sg.Text("Select archive name      ")
input3 = sg.Input()
window = sg.Window("File to compress", layout=[[label1, input1, chose_button1],
                                               [label2, input2, chose_button2],
                                               [label3, input3],
                                               [compress_button]])
while True:
    event, values = window.read()
   #print(event)
    #print(values)
    filepath = values['files'].split(";")
    folder = values["folder"]
    archive_name = values[2]
    #print(archive_name)
    #print(filepath)
    match event:
        case"Compress":
            make_archive(filepath, folder, archive_name)
            window['output'].update(value='Compression completed!')

        case sg.WIN_CLOSED:
            break



