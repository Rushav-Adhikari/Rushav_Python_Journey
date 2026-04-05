'''
Ask user to enter numbers until they type 0
'''

num=""
while num != 0:
    num = int(input("Enter the correct number to win: "))
    if num !=0:
        print(f"{num} is Wrong Try Again!!!")
print("You Won!")
