'''
marks = [78, 92, 65, 88]
Write a program that prints:
    Total Marks: 323
    Average Marks: 80.75
Rules
    ✅ Use a for loop.
    ✅ Use an accumulator variable named total.
    ✅ Use +=.
    ❌ Don't use sum().
'''
# marks = [78, 92, 65, 88]
# total = 0
# for mark in marks:
#     total += mark
# print(f"Total Marks: {total}")

marks = [78, 92, 65, 88]
total = 0
for mark in marks:
    total += mark
print(f"Average Marks: {total/len(marks)}")