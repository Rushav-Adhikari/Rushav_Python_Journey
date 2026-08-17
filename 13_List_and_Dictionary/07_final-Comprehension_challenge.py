prices = [100, 250, 500, 750, 1000, 1500]
discounted_price = [
    price * 0.80
    for price in prices
    if price >= 500
]
print(discounted_price)