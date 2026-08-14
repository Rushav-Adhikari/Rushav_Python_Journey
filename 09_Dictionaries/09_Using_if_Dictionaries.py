employee = {
    "name": "Ram",
    "salary": 60000,
    "department": "Finance"
}

for key, value in employee.items():
    if (key == "salary") and value >= 50000:
        print("Salary is above 50000")