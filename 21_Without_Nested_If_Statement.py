'''
A customer gets a Premium Account if:
    They are 18 or older
    AND
    they have either an income of 50,000+ OR they are an existing premium member.
Use:
    age = 25
    income = 40000
    premium_member = True
Expected output:
    Premium Account
Write it using:
    if
    and
    or
    parentheses
'''

age = 25
income = 40000
premium_member = True
if age >= 18 and (income>=50000 or premium_member):
    print("Premium Account")