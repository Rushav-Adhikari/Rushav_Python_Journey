'''
Question Number 1:
    Create a tuple named fruits containing these items in order:
        Apple
        Banana
        Mango
        Orange
    Then print the tuple.
'''
# fruits = ("Apple", "Banana", "Mango", "Orange")
# print(f"Fruits in Tuple: {fruits}")
# print(f"Type of fruits: {type(fruits)}") # Show the type of the variable fruits

'''
Question Number 2:
Create a tuple named numbers containing these values:
    10, 20, 30, 40, 50
Then:
    Print the first element.
    Print the last element.
⚠️ Challenge: Do not hardcode the index for the last element. Use a Python feature that still works even if the tuple grows or shrinks.
'''
# numbers = (10, 20, 30, 40, 50)
# print(f"First Element: {numbers[0]}") # [0] give the first element.
# print(f"Last Element: {numbers[-1]}") # Negative indexing starts from the end, so -1 always refers to the last element.

'''
Create this tuple:
colors = ("Red", "Blue", "Green", "Yellow", "Black")
    Without printing the whole tuple, print only:
        Blue
        Green
        Black
⚠️ Rule: Use indexing only. Don't type the colour names directly inside print().

For example, don't do:
print("Blue")   # ❌
Use the tuple to access the values.
'''

# colors = ("Red", "Blue", "Green", "Yellow", "Black")
# print(f"This Gives Blue: {colors[1]}")   # # Tuples use zero-based indexing, so index 1 refers to the second element.
# print(f"This Gives Green: {colors[2]}")  # Accessing the third element using index 2
# print(f"This Gives Black: {colors[-1]}")  # Accessing the fifth element using index -1

'''
Question number 4
Now let's learn slicing, which is one of the most useful skills in Python.

Create this tuple:
    colors = ("Red", "Blue", "Green", "Yellow", "Black")
    Your task
Print:
    ("Blue", "Green")
    ("Green", "Yellow", "Black")
⚠️ Rule: Use slicing only.
    Don't use multiple indexes like:
    print(colors[1], colors[2])  # ❌
'''
# colors = ("Red", "Blue", "Green", "Yellow", "Black")
# print(f"Value of Blue and Green using Slicing: {colors[1:3]}")
# print(f"Value of Green, Yellow and Black using Slicing: {colors[2:]}")

'''
Question Number 5
Now let's use a built-in function.
Create this tuple:
    animals = ("Dog", "Cat", "Cow", "Goat", "Horse")
Your tasks
    Print the number of items in the tuple.
    Then print this sentence using an f-string:
    There are 5 animals in the tuple.
⚠️ Challenge: Don't type the number 5 directly in the f-string. Use Python to calculate it.
'''
# animals = ("Dog", "Cat", "Cow", "Goat", "Horse")
# print(len(animals))  # This will print the number of items.
# print(f"There are {len(animals)} animals in the tuple.")


'''
Question Number 6:
This question trips up many beginners.
    Your task
Create a tuple named country that contains only one item:
    Nepal
Then:
    Print the tuple.
    Print its type using type().
⚠️ Don't search online. Try it from memory. This is a very important concept because Python treats a one-item tuple differently from other tuples.
'''
# country = ("Nepal",)  # Note the comma after "Nepal" to indicate it's a tuple with one item.
# print(f"Country Tuple: {country}")  # This will print the tuple containing the string "Nepal".
# print(type(country))  # This will print <class 'tuple'>, confirming that country is indeed a tuple.

'''
Question Number 7:
Create two tuples:
    tuple1 = (1, 2, 3)
    tuple2 = (4, 5, 6)
Your task
    Combine the two tuples into a new tuple called combined.
Print the result.
⚠️ Don't search. Use what you already know. Think about how Python combines sequences.
'''

# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
# new_tuple = tuple1 + tuple2  # This combines the two tuples into a new tuple.
# print(f'Combined Tuples: {new_tuple}')  # This will print the combined tuple (1, 2, 3, 4, 5, 6).

'''
Question Number 8:
Create this tuple:
    letters = ("A", "B", "C", "D", "E")
Your task
    Print the tuple in reverse order using slicing only.
Expected output:
    ('E', 'D', 'C', 'B', 'A')
⚠️ Rule: Do not use reversed() or convert it to a list.
Hint: You've already learned the three parts of slicing:
sequence[start:stop:step]
This question introduces the third part of slicing: step.
'''
letters = ("A", "B", "C", "D", "E")
print(f"Reversed Tuples: {letters[::-1]}")  # The step of -1 reverses the tuple.