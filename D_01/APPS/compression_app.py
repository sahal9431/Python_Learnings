import FreeSimpleGUI as lm

label1 = lm.Text("Select a file to compress")
input_box1 = lm.Input()
choose_dir_button = lm.FileBrowse('Choose File')

label2 = lm.Text("Select destination folder")
input_box2 = lm.Input()
choose_dest_button = lm.FolderBrowse('Choose Folder')

compress_button = lm.Button('Compress')

window = lm.Window('File compression App', 
                   layout=[[label1, input_box1, choose_dir_button], 
                           [label2, input_box2, choose_dest_button], 
                           [compress_button]])
window.read()
window.close()

