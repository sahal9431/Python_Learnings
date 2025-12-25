import FreeSimpleGUI as lm
from D_01.to_do.zip_file_creator import make_zip_file

label1 = lm.Text("Select a file to compress")
input_box1 = lm.Input()
choose_dir_button = lm.FileBrowse('Choose File', key='files')

label2 = lm.Text("Select destination folder")
input_box2 = lm.Input()
choose_dest_button = lm.FolderBrowse('Choose Folder', key='folder')

compress_button = lm.Button('Compress')

window = lm.Window('File compression App', 
                   layout=[[label1, input_box1, choose_dir_button], 
                           [label2, input_box2, choose_dest_button], 
                           [compress_button]])

while True:
    event, values = window.read()
    print(event)
    print(values)
    file_path = values['files'].split(',')
    dest_folder = values['folder']
    make_zip_file(file_path, dest_folder)
        

window.close()

