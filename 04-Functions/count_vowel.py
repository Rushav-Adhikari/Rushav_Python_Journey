'''
6. Count Vowels
Create a function that:
•	takes a string 
•	returns number of vowels (a, e, i, o, u) 

'''

def count_vowels(word):
    vowels = "aeiou"
    count = 0

    for char in word.lower():
        if char in vowels:
            count +=1
    return count

word = input("Enter the words: ")
result = count_vowels(word)
print(f"The words {word} contains {result}")