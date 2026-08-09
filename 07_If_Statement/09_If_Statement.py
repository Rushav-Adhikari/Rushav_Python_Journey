marks = [45, 55, 72, 91]

for mark in marks:
    if mark < 50:
        print(f"{mark} - Fail")
    elif mark < 70:
        print(f"{mark} - Pass")
    elif mark < 90:
        print(f"{mark} - Good")
    else:
        print(f"{mark} - Excellent")