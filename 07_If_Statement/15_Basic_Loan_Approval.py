'''
A bank approves a loan if:
    Income is 50,000 or above
    AND
    Either:
    Credit score is 650 or above, OR
    The customer has a guarantor
Use:
    income = 45000
    credit_score = 620
    has_guarantor = True
Expected output:
    Loan Approved
Rules
    ✅ if
    ✅ and
    ✅ or
    ✅ Parentheses
    ❌ No else yet
'''

income = 45000
credit_score = 620
has_guarantor = True
if income >= 50000 and (credit_score>=650 or has_guarantor):
    print("Loan Approved")
else:
    print("Loan Rejected")