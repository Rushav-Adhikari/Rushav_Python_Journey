'''
sales = [1200, 950, 1800, 750]
Write a program that prints:
    Sales Amount: Rs.1200
    Sales Amount: Rs.950
    Sales Amount: Rs.1800
    Sales Amount: Rs.750
Rules
    ✅ Use a for loop.
    ✅ Use an f-string.
    ❌ No range().
    ❌ No indexing.
'''
sales = [1200, 950, 1800, 750]
for sale in sales:
    print(f"Sales Amount: Rs.{sale}")