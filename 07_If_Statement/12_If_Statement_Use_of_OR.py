'''
A customer gets a discount if:
    Their purchase is 1000 or more, OR
    They are a premium customer.
Use:
    purchase = 700
    premium_customer = True
Write a program that prints:
    Discount Eligible
Rules
    ✅ Use if
    ✅ Use or
    ❌ Don't use and
    ❌ Don't use else yet
'''
purchase = 700
premium_customer = True

if purchase >= 1000 or premium_customer:
    print("Discount Eligible")
else:
    print("No Discount")