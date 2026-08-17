# with open("sales.txt", "w") as file:
#     content = file.write("Product: Laptop \nQuantity: 5 \nPrice: 80000")
# with open("sales.txt", "a") as file:
#     file.write("\nStatus: Completed")

with open("sales.txt", "r") as file:
    content = file.read()
    print(content)
