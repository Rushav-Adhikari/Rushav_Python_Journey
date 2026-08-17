try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    operator = input("Enter Operation (+, -, *, /) :")
    if operator == "+":
        print(f"The addition of the two number is: {num1 + num2}")
    elif operator == "*":
        print(f"The multiplication of the two number is: {num1 * num2}")
    elif operator == "-":
        print(f"The subtraction of the two number is: {num1 - num2}")
    elif operator == "/":
        print(f"The division of the two number is: {num1 / num2}")
    else:
        print("Please enter valid operation")
except ValueError:
    print("Please enter valid number.")
except ZeroDivisionError:
    print("Cannot Divide by zero.")