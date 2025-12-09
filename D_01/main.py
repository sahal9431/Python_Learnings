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

# members = ["john", "sarah", "dora"]
# for member in members:
#     member = member.capitalize()
#     print(member)

# file_names = ['1.abc.txt', '2.qwe.txt', '3.wer.txt']
# for filename in file_names:
#     file_name = filename.replace('.', '-', 1)
#     print(file_name)
# file_names = ('1.abc.txt', '2.qwe.txt', '3.wer.txt')
# print(type(file_names))

contents = ['running race', 'car racing', 'boat racing']
filenames = ['human.txt', 'landtransport.txt', 'watertransport.txt']
for content, filename in zip(contents, filenames):
    file = open(f"D_01/files/{filename}", 'w')
    file.write(content)
