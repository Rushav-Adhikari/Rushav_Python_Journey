'''
1. Greeting Function

Create a function that:

takes a name
prints: "Hello <name>"
'''


def greet(name):
    return f"Hello, {name}, Welcome to Data Science."

name = input("Enter your name: ")
message = greet(name)
print(message)