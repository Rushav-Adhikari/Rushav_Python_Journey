'''
A student's grade is classified as:
    80 or above → A
    60–79 → B
    50–59 → C
    Below 50 → Fail
Use:
    marks = [85, 72, 58, 91, 43, 67]
Expected output:
    85 - A
    72 - B
    58 - C
    91 - A
    43 - Fail
    67 - B
Rules
    ✅ for
    ✅ if
    ✅ elif
    ✅ else
    ✅ f-string
    ❌ No range()
'''
marks = [85, 72, 58, 91, 43, 67]
for mark in marks:
    if mark >= 80:
        print(f"{mark} - A")
    elif mark >= 60:
        print(f"{mark} - B")
    elif mark >= 50:
        print(f"{mark} - C")
    else:
        print(f"{mark} - Fail")