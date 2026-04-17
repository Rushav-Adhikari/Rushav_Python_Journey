'''
8. Average Calculator
Create a function:
•	input: list of numbers 
•	return: average 

'''

def average(numbs):
    return sum(numbs)/len(numbs)

numbs = list(map(int, input("Enter a number: ").split()))
result = average(numbs)

print(f"The Average of {numbs} is {result}")