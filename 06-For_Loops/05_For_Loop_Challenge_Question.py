'''
numbers = [2, 4, 6, 8]
Write a for loop that prints:
    The number is 2
    The number is 4
    The number is 6
    The number is 8
    Loop Finished
⚠️ Notice carefully:
"The number is ..." should be printed for every number.
"Loop Finished" should be printed only once, after the loop ends.
'''
numbers = [2, 4, 6, 8]
for number in numbers:
    print(f"The number is {number}")
print("Loop Finished")