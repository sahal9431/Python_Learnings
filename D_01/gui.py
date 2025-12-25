import functions
import FreeSimpleGUI as lm

label = lm.Text("Type a TO_DO")
input_box = lm.InputText(tooltip="Enter TODO")
add_button = lm.Button('Add')
edit_button = lm.Button('Edit')
remove_button = lm.Button('Remove')

window = lm.Window('My T0-Do App', layout=[[label], [input_box, add_button], [edit_button, remove_button] ])
window.read()
window.close()
