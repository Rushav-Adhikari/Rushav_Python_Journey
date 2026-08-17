try:
    user = int(input("Enter your age: "))
    print(f"Your age is {user}")
except ValueError:
    print("Please enter a valid age.")