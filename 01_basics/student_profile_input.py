'''
***Trying Input and If Elif and Else.
Ask the user to enter their name, age, country
Ask the user to enter marks in 3 subjects
Calculate total and average
Print a combined sentence like:
Hello [name] from [country], you scored [total] marks with an average of [average].
Check pass/fail (average >= 50 → pass)
Print first & last letter of the name
'''

name = input("Enter Your Name: ")
age = int(input("Enter Your Age: "))
country = input("Where Do You Live: ")
math = int(input("Enter your marks on Math: "))
science = int(input("Enter your marks on Science: "))
english = int(input("Enter your marks on English: "))
total_mark = math + science + english
avg_mark = total_mark/3
print(f'Hello! Your name is {name} and you are from {country}, you scored total {total_mark} marks with an average of {avg_mark:.2f}.')

print("***Checking either you are passed or failed!!!***")

if math >=50 and science>=50 and english>=50:
    print("You are Passed!")
else:
    print("You are Failed!. Better Luck Next Time")

print(f"First Letter of your name is {name[0]}")
print(f"Last Letter of your name is {name[-1]}")