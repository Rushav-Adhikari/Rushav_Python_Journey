'''
A teacher wants to know which students passed.
Passing marks are 50 or above.
Use this list:
    marks = [78, 45, 92, 33, 65]
Instead, write a program that prints every mark in this format:
    Student Mark: 78
    Student Mark: 45
    Student Mark: 92
    Student Mark: 33
    Student Mark: 65
'''
marks = [78, 45, 92, 33, 65]
for mark in marks:
    print(f"Student Mark: {mark}")