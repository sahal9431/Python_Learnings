import FreeSimpleGUI as lm
from ..to_do import functions
import time
import os

if not os.path.exists("todos.txt"): # Create the file if it doesn't exist
    with open("todos.txt", "w") as file:
        pass

lm.theme('DarkPurple4')
label = lm.Text("Type a TO_DO")
input_box = lm.InputText(tooltip="Enter TODO", key="todo")
add_button = lm.Button('Add')
edit_button = lm.Button('Edit')
remove_button = lm.Button('Remove')
exit_button = lm.Button('Exit')
clock = lm.Text('', key='clock')
list_box = lm.Listbox(values=functions.get_todos(), 
                      key='todos',
                      enable_events=True, size=[45, 10])
layout = [[label], 
          [clock],
          [input_box, add_button], 
          [list_box, edit_button], 
          [remove_button], 
          [exit_button]]
window = lm.Window('My T0-Do App', 
                   layout=layout, 
                           font=('Times New Roman', 20))
while True:
    event, values = window.read(timeout=10)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    # print(event)
    # print(values)
    # print(values['todos'])
    match event:
        case 'Add':
            todos = functions.get_todos()
            todos.append(values['todo'] + '\n')
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + '\n'
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                lm.popup("Please select an item first", 
                         font=('Times New Roman', 20))
        case 'todos': # Listbox selected
            window['todo'].update(value=values['todos'][0])
        case 'Remove':
            try:
                todo_to_remove = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_remove)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='') # Clear input box
            except IndexError:
                lm.popup("Please select an item first", 
                         font=('Times New Roman', 20))
        case 'Exit':
            break
        case lm.WIN_CLOSED:
            break
print('Bye!')
window.close()
