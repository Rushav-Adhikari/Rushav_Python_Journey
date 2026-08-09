'''
Ask the user for:
    Age
    Monthly Income
    Credit Score
Rules:
    Age must be 18 or above
If age is valid:
    Income must be 50,000 or above
If income is valid:
    Credit score must be 650 or above
If all three pass → "Loan Approved"
Otherwise:
    Under 18 → "Age Requirement Not Met"
    Low income → "Income Too Low"
    Low credit score → "Credit Score Too Low"
Restrictions
    ✅ Use nested if
    ✅ Use else
    ❌ Don't use and
    ❌ Don't use or
    ❌ Don't use elif
'''
age = int(input("Enter the Age: "))
monthly_income = int(input("Enter the Monthly Income: "))
credit_score = int(input("Enter the Credit Score: "))
if age >=18:
    if monthly_income>= 50000:
        if credit_score >= 650:
            print("Loan Approved")
        else:
            print("Credit Score Too Low")
    else:
        print("Income Too Low")
else:
    print("Age Requirement Not Met")
