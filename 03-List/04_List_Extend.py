'''
💻 Practice Question 3 (Last question for today)
skills = ["Excel", "SQL"]
Create another list:
    new_skills = ["Python", "Power BI"]
Now:
    Print the original skills list.
    Use extend() to add all the items from new_skills.
    Print the updated skills list.
'''
skills = ["Excel", "SQL"]
new_skills = ["Python", "Power BI"]
print(f"Original List: {skills}")
skills.extend(new_skills)
print(f"Extended Skills: {skills}")