'''
Day 1 of Practicing Python
Create a program where you store the following details:

Your name
Your age
Your country
Marks in 3 subjects (Math, Science, English)
A boolean value: is_student = True
'''

name = 'Rushav Adhikari'
age = 26
country = "Nepal"
marks_math = 56
marks_science = 80
marks_english = 85
is_student = True
total_mark = (marks_math + marks_english + marks_science)
avg = total_mark/3

# print("Your Name is: ",name)
# print("And you are:", age, "years old")
# print("The country you lived in:", country)
# print("You got", marks_math, "in Math.")
# print("You got", marks_science, "in Science.")
# print("You got", marks_english, "in English.")
# print("Your Total Mark is:", total_mark )
# print("Your Average Mark is: ",avg)
# print("Am i Student ?", is_student)

print(f"My Name is {name} and I am from {country}. I am {age} years old.")

print(f"My total marks is {total_mark} and My average marks is {avg:.2f}.")

print(f"Am I Student? {is_student}.")

print(f"First letter of my name: {name[0]}")
print(f"Last letter of my name: {name[-1]}")