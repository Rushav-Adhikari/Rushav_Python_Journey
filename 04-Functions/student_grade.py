'''
. Student Grade Function
Create a function:
•	input: marks 
•	output: 
o	80+ → "A" 
o	60–79 → "B" 
o	below 60 → "C" 

'''

def calculate_grade(marks):
    if marks < 0 or marks > 100:
        return "Invalid Marks"
    elif marks >= 80:
        return "A"
    elif marks >=60:
        return "B"
    else:
        return "C"

marks = int(input("Enter the marks: "))
result = calculate_grade(marks)
print(f"You scored {marks} and your grade is {result}")