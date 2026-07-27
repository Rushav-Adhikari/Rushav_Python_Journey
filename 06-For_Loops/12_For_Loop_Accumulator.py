'''
Use this list:
sales = [1200, 950, 1800, 750]
Expected output:
    Total Sales: Rs.4700
Rules
    ✅ Use a for loop.
    ✅ Create a variable named total and initialize it to 0.
    ✅ Add each sale to total.
    ✅ Print the final total using an f-string.
    ❌ Don't use Python's built-in sum() function (we'll learn that later).
'''
sales = [1200, 950, 1800, 750]
total = 0
for sale in sales:
    total += sale
print(f"Total Sales: Rs.{total}")