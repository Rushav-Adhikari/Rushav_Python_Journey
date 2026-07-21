'''
Question 3 (Medium)
Given:
marks = (75, 82, 91, 68, 85)
Find and print:
    Highest mark
    Lowest mark
    Sum of all marks
    Average mark
Hint: Use built-in functions like max(), min(), sum(), and len().
'''

marks = (75, 82, 91, 68, 85)
avg = sum(marks)/len(marks)

print(f"Highest Mark:", max(marks))
print(f"Lowest Mark:", min(marks))
print(f"Sum of all Marks:", sum(marks))
print(f"Average Marks:", avg)