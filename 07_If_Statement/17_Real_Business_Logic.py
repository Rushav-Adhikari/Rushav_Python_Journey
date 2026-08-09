'''
A bank wants to evaluate a customer:
    age = 30
    income = 60000
Rules:
    If age is 18 or above, continue checking.
    If income is 50,000 or above → "Loan Eligible"
    Otherwise → "Income Too Low"
    If age is below 18 → "Age Requirement Not Met"
'''
age = int(input("Enter your Age:"))
income = int(input("Enter your Monthly Income:"))
if age >=18:
    if income>=50000:
        print("Eligible")
    else:
        print("Income Too Low")
else:
    print("Age Requirement Not Met")