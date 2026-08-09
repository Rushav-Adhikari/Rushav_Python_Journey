'''
A bank gives a special loan offer when:
Customer has income of 50,000 or more
    AND
they either have a credit score of 700 or more OR they have a guarantor.
    income = 60000
    credit_score = 680
    has_guarantor = True
'''
income = 60000
credit_score = 680
has_guarantor = True
if income >= 50000:
    if credit_score >= 700 or has_guarantor:
        print("Special Loan Offer")
    else:
        print("Check Your Credit Score or Guarantor")
else:
    print("Low Income")