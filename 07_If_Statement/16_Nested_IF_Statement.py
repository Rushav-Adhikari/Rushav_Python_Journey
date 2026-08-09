'''
A bank allows a customer to apply for a loan only if:
    Their age is 18 or above
    If they are 18+, they must have a valid ID.
Use:
    age = 25
    has_id = True
Write a program that prints:
    Loan Application Allowed
Rules
    ✅ Use a nested if
    ✅ Use two if statements
    ❌ Don't use and
    ❌ Don't use elif yet
'''
# age = 25
# has_id = False

# if age >=18:
#     if has_id:
#         print("Loan Application Allowed")

'''
A company checks an employee before allowing access:
    If the employee is 18 or older
    If they have an ID → "Access Granted"
    Otherwise → "ID Required"
    If they are under 18 → no output
Use:
    age = 25
    has_id = False
Expected output:
    ID Required
Rules
    ✅ Nested if
    ✅ Inner else
    ❌ No and
    ❌ No elif
'''

# age = 25
# has_id = False

# if age >=18:
#     if has_id:print("Access Granted")
#     else: print("ID Required")
        

age = 16
has_id = True

if age >=18:
    if has_id:
        print("Access Granted")
    else:
        print("ID Required")
else:
    print("Underage")