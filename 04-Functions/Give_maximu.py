'''
4. Maximum of Two Numbers

Create a function that:

takes 2 numbers
returns the larger number
'''

def max_number(num1, num2):
    return num1 if num1 > num2 else num2

num1 = int(input("Enter the num1: "))
num2 = int(input("Enter the num2: "))
max_value = max_number(num1, num2)
print(f"The Maximum number between two number {num1} and {num2} is {max_value}")