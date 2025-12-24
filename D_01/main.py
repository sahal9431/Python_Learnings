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

# contents = ['running race', 'car racing', 'boat racing']
# filenames = ['human.txt', 'landtransport.txt', 'watertransport.txt']
# for content, filename in zip(contents, filenames):
#     file = open(f"D_01/files/{filename}", 'w')
#     file.write(content)

# Sterght of password checker
# password = input("Enter password: ")
# result = []
# if len(password) >= 8:
#     result.append(True)
# else:
#     result.append(False)

# digit = False
# for i in password:
#     if i.isdigit():
#         digit = True
# result.append(digit)

# uppercase = False
# for i in password:
#     if i.isdigit():
#         uppercase = True
# result.append(uppercase)

# #print(all(result))
# if all(result):
#     print("Strong password")
# else:
#     print("Weak password")

#dictionary
# user = {
#     "username": "john",
#     "password": "1234",
# }
# print("username" in user)

# def get_average():
#     with open('source.txt', 'r') as file:
#         numbers = file.readlines()
#     values = numbers[1:]
#     values = [float(i) for i in values]
#     print(values)
#     average_local = sum(values) / len(values)
#     return average_local

# average = get_average()
# print(average)

# def get_max():
#     grades = [9.6, 9.2, 9.7]
#     maximum = float(max(grades))
#     minimum = float(min(grades))
#     print(f"Max:{maximum}, Min:{minimum}")
#     return maximum, minimum

# get_max()

# def format_filename():
#     filename = "report.txt"
#     filename = filename[:-4].capitalize()
#     print(filename)
#     return filename
    
# format_filename()

# def square_number():
#     number = 5
#     number = number * 5
#     print(number)
#     return number

# square_number()

#Decoupling is the process of splitting function to reduce dependencies between them.
# feet_inches = input("Enter feet and inches separated by space: ")

# def converstion(feet_inches):
#     feet, inches = feet_inches.split() # Split input into feet and inches
#     feet = float(feet) # Convert feet to float
#     inches = float(inches) # Convert inches to float
#     total_inches = (feet * 12) + inches # Calculate total inches
#     cm = total_inches * 2.54 # Convert inches to centimeters
#     print(f"{feet} feet and {inches} inches equal to {cm} cm") # Print result
#     return

# converstion(feet_inches)

# def foo(name):
#     """Returns a greeting message for the given name."""
#     return f"Hi {name}"
# foo("sanju")

#glob modules defenition is used to define variables that can be used across multiple functions within the same module.
# import glob

# myfiles = glob.glob("D_01/files/*.txt")
# print(myfiles)

# import csv
# # csv definition is used to read and write data in CSV (Comma Separated Values) format.

# import shutil
# # shutil definition is used for high-level file operations such as copying and moving files and directories.
# shutil.make_archive('output', 'zip', 'D_01/files') # Create a zip archive of the 'files' directory named 'output.zip'

# import webbrowser
# # webbrowser definition is used to open web pages in the default web browser.
# webbrowser.open('https://www.google.com') # Open Google in the default web browser

# a = [{"Question": "what are dolphins", "Options": ["Amphibians", "Mammals", "Reptiles"], "Answer": "2"}, 
#      {"Question": "what are elephants", "Options": ["Amphibians", "Mammals", "Reptiles"], "Answer": "1"}]

# import json
# with open('D_01/questions.json', 'r') as file:
#     question = file.read()

# data = json.loads(question)
# score = 0
# for question in data:
#     print(question["Question"])
#     for index, option in enumerate(question["Options"]):
#         print(index + 1, "-", option)
#     answer = input("Enter your answer (1/2/3): ")
#     question["answer"] = answer
#     print(question["answer"])
#     if question["answer"] == question["Answer"]:
#         score += 1
#         #print(f"Your score is: {score}/{len(data)}")
# for index, question in enumerate(data):
#     message = f'{index + 1} - "Your answer:" {question["answer"]}, \
#     "Correct answer:" {question["Answer"]}'
#     print(message)
# print(f"Your score is: {score}/{len(data)}")

# import random
# number_1 = input("Enter first number: ")
# number_2 = input("Enter second number: ")

# randum_number = random.randint(int(number_1), int(number_2)) # Generate random number between number_1 and number_2
# print(randum_number)



