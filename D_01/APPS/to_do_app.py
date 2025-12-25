import FreeSimpleGUI as lm
from D_01.to_do import functions

label = lm.Text("Type a TO_DO")
input_box = lm.InputText(tooltip="Enter TODO", key="todo")
add_button = lm.Button('Add')
edit_button = lm.Button('Edit')
show_button = lm.Button('Show')
remove_button = lm.Button('Remove')
list_box = lm.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
layout = [[label], 
          [input_box, add_button], 
          [list_box, edit_button], 
          [show_button], 
          [remove_button]]
window = lm.Window('My T0-Do App', 
                   layout=layout, 
                           font=('Times New Roman', 20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    print(values['todos'])
    match event:
        case 'Add':
            todos = functions.get_todos()
            todos.append(values['todo'] + '\n')
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + '\n'
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'todos': # Listbox selected
            window['todo'].update(value=values['todos'][0])
        case lm.WIN_CLOSED:
            break
print('Bye!')
window.close()
