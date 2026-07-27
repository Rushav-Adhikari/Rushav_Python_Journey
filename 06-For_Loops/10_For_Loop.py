'''
marks = [78, 92, 65, 88]
Write a program that prints:
    Student scored: 78
    Student scored: 92
    Student scored: 65
    Student scored: 88
Rules
    ✅ Use a for loop.
    ✅ Use an f-string.
    ❌ Don't use range().
    ❌ Don't use indexing.
'''
marks = [78, 92, 65, 88]
for mark in marks:
    print(f"Student Scored: {mark}")
    