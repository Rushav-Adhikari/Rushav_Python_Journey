'''
A company categorizes sales like this:
    1000 or above → High Sale
    Below 1000 → Low Sale
Use:
    sales = [500, 1200, 300, 1800, 750, 2500]
Expected output:
    500 - Low Sale
    1200 - High Sale
    300 - Low Sale
    1800 - High Sale
    750 - Low Sale
    2500 - High Sale
Rules
    ✅ for
    ✅ if
    ✅ else
    ✅ >=
    ✅ f-string
    ❌ No range()
'''
sales = [500, 1200, 300, 1800, 750, 2500]
for sale in sales:
    if sale >=1000:
        print(f"{sale} - High Sale")
    else:
        print(f"{sale} - Low Sale")