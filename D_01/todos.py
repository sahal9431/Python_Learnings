def get_todos(file_path = 'todos.txt'): # Function to read todos from file 
    with open(file_path, 'r') as file:
        todos_local = file.readlines()
    return todos_local # Return the list of todos


def write_todos(todos_arg, filepath= 'todos.txt'): # Function to write todos to file
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


#todos = []
while True:
    user_input = input("Select Add,Show,Edit,Remove or Exit:")
    user_input = user_input.lower().strip() # Normalize input by converting to lowercase and removing extra spaces

    if user_input.startswith("add"): # Check if 'add' is in the input
        #todo = input("Enter To Do: ") + "\n" # Add newline character
        todo = user_input[4:] + "\n" # Extract todo from input string
        # Option_1: 
        # file = open('todos.txt', 'r') # Read existing todos
        # todos = file.readlines() # Read lines into list
        # file.close() # Close file

        #Option_2: # With file handling
        # with open('todos.txt', 'r') as file: # Open file using context manager
        #     todos = file.readlines() # Read existing todos
        todos = get_todos() # Get existing todos using function

        todos.append(todo) # Add new todo to list

        #Option_1:
        # file = open('todos.txt', 'w') # Open file in write mode
        # file.writelines(todos) # Write updated todos back to file
        # file.close()

        #Option_2:
        # with open('todos.txt', 'w') as file: # Open file in write mode using context manager
        #     file.writelines(todos) # Write updated todos back to file
        write_todos(filepath='todos.txt', todos_arg=todos) # Write updated todos using function

    elif "show" in user_input: # Check if 'show' is in the input
        file = open('todos.txt', 'r')
        todos = file.readlines()
        file.close()
        #Option_1
        # new_todos = [] # Create new list
        # for item in todos: # Iterate through existing todos
        #     item = item.strip('\n') # Remove newline character
        #     new_todos.append(item) # Create new list without newline characters
        #Option_2
        #new_todos = [item.strip('\n') for item in todos] # List comprehension to remove newline characters

        for index, item in enumerate(todos): #enumerate gives index and item
            #print(index, '-', item) # Display index and item
            #Option_3_Improved
            item = item.title().strip('\n') # Capitalize item and remove newline
            print(f"{index + 1}-{item}") # f-string formatting

    elif "edit" in user_input: # Check if 'edit' is in the input
        try:
            #number = int(input("number of to todo to edit: "))
            number = int(user_input[5:]) # Extract number from input string
            number = number - 1 # Convert to zero-based index

            # with open('todos.txt', 'r') as file: # Open file using context manager
            #     todos = file.readlines() # Read existing todos
            todos = get_todos() # Get existing todos using function

            new_todo = input("Enter new todo: ") # Get new todo from user
            new_todo = new_todo.title() # Capitalize new todo

            todos[number] = new_todo # Update the todo at the specified index

            # with open('todos.txt', 'w') as file: # Open file in write mode using context manager
            #     file.writelines(todos) # Write updated todos back to file
            write_todos(filepath='todos.txt', todos_arg=todos) # Write updated todos using function
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

    elif "exit" in user_input: # Check if 'exit' is in the input
        break

    elif "remove" in user_input: # Check if 'complete' or 'Remove' is in the input
        try:
            #number = int(input("number of to todo to complete: "))
            number = int(user_input[7:]) # Extract number from input string

            # with open('todos.txt', 'r') as file: # Open file using context manager
            #     todos = file.readlines() # Read existing todos
            todos = get_todos() # Get existing todos using function

            number = number - 1 # Convert to zero-based index
            todo_to_remove = todos[number].strip('\n') # Get the todo to be removed and strip newline
            todos.pop(number) # Remove the todo at the specified index

            # with open('todos.txt', 'w') as file: # Open file in write mode using context manager
            #     file.writelines(todos) # Write updated todos back to file
            write_todos(filepath='todos.txt', todos_arg=todos) # Write updated todos using function
            
            print(f"Todo '{todo_to_remove}' removed from the list.")
        except IndexError:
            print("Invalid todo number. Please try again.")
            continue
    else:
        print("Command not recognized.")

print("Goodbye!")