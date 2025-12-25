import FreeSimpleGUI as lm

label1 = lm.Text("Enter feet: ")
inputbox1 = lm.Input(key='feet')
label2 = lm.Text("Enter inches: ")
inputbox2 = lm.Input(key='inches')
convert_button = lm.Button('Convert')
result = lm.Text("", key='result') # To display the result
layout = [[label1, inputbox1],[label2, inputbox2],[convert_button, result]]
window = lm.Window('Converter', layout= layout, font=('Times New Roman', 20))
while True:
    event, values = window.read()
    match event:
        case 'Convert':
            feet = float(values['feet'])
            inches = float(values['inches'])
            meters = feet * 0.3048 + inches * 0.0254
            #lm.popup(f'{feet} feet and {inches} inches is {meters} meters') # Show popup with result
            window['result'].update(f"{meters} m")
        case lm.WIN_CLOSED:
            break
window.close()