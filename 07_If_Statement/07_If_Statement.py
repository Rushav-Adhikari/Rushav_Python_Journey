'''
Use:
    sales = [500, 1200, 300, 1800, 750, 2500]
Classify each sale:
    2000 or above → Excellent
    1000 or above → Good
    Otherwise → Low
Expected output:
    500 - Low
    1200 - Good
    300 - Low
    1800 - Good
    750 - Low
    2500 - Excellent
Rules
    ✅ Use for
    ✅ Use if
    ✅ Use elif
    ✅ Use else
    ✅ Use an f-string
    ❌ Don't use range()
'''
sales = [500, 1200, 300, 1800, 750, 2500]
for sale in sales:
    if sale >=2000:
        print(f"{sale} - Excellent")
    elif sale >= 1000:
        print(f"{sale} - Good")
    else: 
        print(f"{sale} - Low")