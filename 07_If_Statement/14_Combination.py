'''
Use:
    marks = 72
    attendance = 65
    recommendation = True
The student is eligible if:
    Marks are 70 or above
    AND
    Attendance is 75 or above OR recommendation is True
Write a program that prints:
    Eligible
Rules
    ✅ Use if
    ✅ Use and
    ✅ Use or
    ✅ Use parentheses
    ❌ Don't use else yet
'''
marks = 72
attendance = 65
recommendation = True
if marks >= 70 and (attendance >=75 or recommendation):
    print("Eligible")

