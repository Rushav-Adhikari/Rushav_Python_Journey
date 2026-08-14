# employees = {
#     "employee1": {
#         "name": "Ram",
#         "salary": 60000,
#         "department": "Finance"
#     },
#     "employee2": {
#         "name": "Sita",
#         "salary": 55000,
#         "department": "HR"
#     }
# }
# print(employees["employee1"]["department"])

# employees = {
#     "employee1": {
#         "name": "Ram",
#         "salary": 60000,
#         "department": "Finance"
#     },
#     "employee2": {
#         "name": "Sita",
#         "salary": 55000,
#         "department": "HR"
#     }
# }
# for employee_id, details in employees.items():
#     print(details["name"], ":", details["department"])
#     # or
#     print(f"{details['name']} : {details['department']}")

employees = {
    "employee1": {
        "name": "Ram",
        "salary": 60000,
        "department": "Finance"
    },
    "employee2": {
        "name": "Sita",
        "salary": 45000,
        "department": "HR"
    }
}

for employee_id, details in employees.items():
    if details["salary"] >= 50000:
        print(f"{details['name']} : {details['salary']}")