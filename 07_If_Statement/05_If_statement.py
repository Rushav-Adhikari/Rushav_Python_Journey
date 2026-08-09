'''
Use:
    marks = [78, 45, 92, 33, 65]
Write a program that prints:
    78 - Pass
    45 - Fail
    92 - Pass
    33 - Fail
    65 - Pass
Rules
    ✅ Use a for loop.
    ✅ Use if.
    ✅ Use else.
    ✅ Passing mark = 50 or above.
    ✅ Use an f-string.
    ❌ Don't use range().
'''
marks = [78, 45, 92, 33, 65]
for mark in marks:
    if mark >= 50:
        print(f"{mark} - Pass")
    else:
        print(f"{mark} - Fail")