'''
A student can receive a certificate only if:
    Marks are 50 or above
    Attendance is 75 or above
Use:
    marks = 72
    attendance = 80
Write a program that prints:
    Certificate Eligible
Rules
    ✅ Use if
    ✅ Use and
    ✅ Use both conditions
    ❌ Don't use else yet
'''
marks = 72
attendance = 80
if marks >= 50 and attendance >= 75:
    print("Certificate Eligible")

'''
marks = 72
attendance = 65
The requirement is still:
    Marks ≥ 50
    Attendance ≥ 75
Write the program so that it prints:
    Not Eligible
Rules
    ✅ Use if
    ✅ Use else
    ✅ Use and
    ❌ Don't change the requirements.
'''
marks = 72
attendance = 65
if marks >= 50 and attendance >= 75:
    print("Eligible")
else:
    print("Not Eligible")