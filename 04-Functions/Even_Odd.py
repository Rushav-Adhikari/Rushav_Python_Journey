'''
3. Even or Odd

Create a function that:

takes a number
returns "Even" or "Odd"
'''

def even_odd(number):
    return "Even" if number %2==0 else "odd"

number = int(input("Enter the number: "))
ev_od = even_odd(number)  # ev = even and od = odd
print(f"The number you provided {number} is {ev_od}")