'''
sales = [500, 1200, 300, 1800, 750, 2500]
A company considers a sale "High Sale" if it is 1000 or above.
Write a program that prints only the high sales.
Expected output:
    1200
    1800
    2500
Rules
    ✅ Use for
    ✅ Use if
    ✅ Use >=
    ❌ No else
    ❌ No range()
'''
sales = [500, 1200, 300, 1800, 750, 2500]
for sale in sales:
    if sale >= 1000:
        print(sale)