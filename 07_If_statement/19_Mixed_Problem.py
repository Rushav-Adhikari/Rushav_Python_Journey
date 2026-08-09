'''
You have this sales data:
    sales = [450, 1200, 750, 2500, 1800, 300]
A company wants to classify each sale:
    Below 500 → Very Low
    500–999 → Low
    1000–1999 → Good
    2000+ → Excellent
But there's one additional rule:
    A sale is considered "Priority" if it is 1000+ AND it is Excellent or Good.
'''
sales = [450, 1200, 750, 2500, 1800, 300]
for sale in sales:
    if sale < 500:
        print(f"{sale} - Very Low")
    elif sale < 1000:
        print(f"{sale} - Low")
    elif sale < 2000:
        print(f"{sale} - Good - Priority")
    else:
        print(f"{sale} - Excellent - Priority")
