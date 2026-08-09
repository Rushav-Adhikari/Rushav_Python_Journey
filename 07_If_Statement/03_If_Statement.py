'''
Use:
    marks = [78, 45, 92, 33, 65]
Write a program that prints only the marks that are 50 or above.
Expected output:
    78
    92
    65
Rules
    ✅ Use a for loop.
    ✅ Use an if statement.
    ✅ Use >= 50.
    ❌ Don't use else yet.
    ❌ Don't use range().
    ❌ Don't manually print the answers.
'''
marks = [78, 45, 92, 33, 65]
for mark in marks:
    if mark>=50:
        print(mark)