try:
    num1 = int(input("Enter the 1st number: "))
    num2 = int(input("Enter the 2nd number: "))
    result = num1 /  num2
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Please enter the valid number.")
