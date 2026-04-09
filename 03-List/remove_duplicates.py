'''
marks = [85, 42, 90, 67, 42, 75, 90, 30]
Remove all duplicate values
'''

# marks = [85, 42, 90, 67, 42, 75, 90, 30]
# new_marks = []

# for i in marks:
#     if i not in new_marks:
#         new_marks.append(i)
# print(new_marks)

'''
colors = ["red", "blue", "red", "green", "blue"]
👉 Remove duplicates while keeping the original order
'''

# colors = ["red", "blue", "red", "green", "blue"]
# new_colors = []
# print(colors)
# for color in colors:
#     if color not in new_colors:
#         new_colors.append(color)
# print(new_colors)


"""
marks = [40, 50, 40, 60, 70, 60, 80]
👉 Remove duplicates AND only keep values greater than 50
"""
# marks = [40, 50, 40, 60, 70, 60, 80]
# g_mark = []
# print(marks)
# for mark in marks:
#     if mark not in g_mark:
#         if mark > 50:
#             g_mark.append(mark)
# print(g_mark)


''''
👉 Create a list of only duplicated values
'''
# nums = [10, 20, 10, 30, 20, 40]
# seen = []
# du_num = []
# print(nums)

# for num in nums:
#     if num in seen:
#         if num not in du_num:
#             du_num.append(num)
#     else:
#         seen.append(num)
# print(du_num)


'''
👉 Remove duplicates AND return list in sorted order
'''

# nums = [3, 1, 2, 3, 4, 1, 5]
# new_nums = []

# for num in nums:
#     if num not in new_nums:
#         new_nums.append(num)
# new_nums.sort()
# print(new_nums)


'''
👉 Remove duplicates AND keep descending order
'''
nums = [3, 1, 2, 3, 4, 1, 5]
number = []

for num in nums:
    if num not in number:
        number.append(num)
number.sort(reverse=True)
print(number)