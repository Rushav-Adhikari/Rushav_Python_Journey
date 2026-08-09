'''
A company has the following sales:
    sales = [450, 1200, 750, 2500, 1800, 300]
Classify each sale:

    < 500 → Very Low
    500–999 → Low
    1000–1999 → Good
    2000+ → Excellent

Expected output:
    450 - Very Low
    1200 - Good
    750 - Low
    2500 - Excellent
    1800 - Good
    300 - Very Low
Rules
    ✅ for
    ✅ if
    ✅ elif
    ✅ else
    ✅ f-string
    ❌ No range()
'''
sales = [450, 1200, 750, 2500, 1800, 300]
for sale in sales:
    if sale < 500:
        print(f"{sale} - Very Low")
    elif sale < 1000:
        print(f"{sale} - Low")
    elif sale < 2000:
        print(f"{sale} - Good")
    else:
        print(f"{sale} - Excellent")