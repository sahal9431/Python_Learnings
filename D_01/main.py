# User_prompt = "Enter To Do: "
# todo1 = input(User_prompt)
# todo2 = input(User_prompt)
# todo3 = input(User_prompt)
# todos = [todo1, todo2, todo3]
# print(todos)
# print(type(todos))
# print("Lenght of variable", len(todo1))

# User_prompt = "Enter To Do: "
# todos = [] # Empty list
# while True:
#     todo = input(User_prompt)
#     todo = todo.capitalize() # Make first letter uppercase
#     todo = todo.title()      # Make first letter of each word uppercase
#     todos.append(todo)  # Add todo to list
#     print(todos)

# password = input("Enter password: ")
# while password != "123":
#     print("Wrong password!")
#     password = input("Enter password: ")
# print("Password accepted!")

# x = 1
# while x <= 6:
#     print(x)
#     x += 1

# print(dir(list))
# print(help(list.count))

todos = []
while True:
    user_input = input("Select ADD,SHOW and EXIT: ")
    user_input = user_input.lower()
    match user_input:
        case "add":
            todo = input("Enter To Do: ")
            todo = todo.capitalize()
            todos.append(todo)
        case "show":
            for item in todos:
                print(item)
        case 'exit':
            break
        case whatever:
            print("Unknown command")
print("Goodbye!")

# members = ["john", "sarah", "dora"]
# for member in members:
#     member = member.capitalize()
#     print(member)

