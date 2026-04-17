'''
2. Square Number

Create a function that:

takes a number
returns its square

👉 Example:
input: 4 → output: 16
'''

def sq_num(number):
    return number*number


number = int(input("Enter the number to make a square: "))
result = sq_num(number)
print(f"The Square of {number} is {result}.")