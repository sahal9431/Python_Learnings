FILE_PATH = 'D_01/TO_DO/todos.txt'

def get_todos(file_path = FILE_PATH):
    """Reads the todo items from the specified file and returns them as a list."""
    with open(file_path, 'r') as file:
        todos_local = file.readlines()
    return todos_local # Return the list of todos


def write_todos(todos_arg, filepath= FILE_PATH):
    """Writes the given list of todo items to the specified file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("functions.py is being run directly")