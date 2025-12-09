
#todos = []
while True:
    user_input = input("Select ADD,SHOW,edit,complete and EXIT: ")
    user_input = user_input.lower().strip() # Normalize input by converting to lowercase and removing extra spaces
    match user_input:
        case "add":
            todo = input("Enter To Do: ") + "\n"
            todo = todo.capitalize()

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case "show" | "display": #add multiple options
            for index, item in enumerate(todos): #enumerate gives index and item
                file = open('todos.txt', 'r')
                todos = file.readlines()
                file.close()
                
                #print(index, '-', item) # Display index and item
                print(f"{index + 1}-{item}") # f-string formatting
        case 'edit':
            number = int(input("number of to todo to edit: "))
            number = number - 1 # Convert to zero-based index
            new_todo = input("Enter new todo: ") # Get new todo from user
            new_todo = new_todo.title() # Capitalize new todo
            todos[number] = new_todo # Update the todo at the specified index
        case 'exit':
            break
        case 'complete':
            number = int(input("number of to todo to complete: "))
            number = number - 1 # Convert to zero-based index
            todos.pop(number) # Remove the todo at the specified index
        case _: # Default case
            print("Unknown command")
print("Goodbye!")