# squares = {num: num ** 2 for num in range(1,6)}
# print(squares)

salaries = {
    "Ram": 45000,
    "Sita": 60000,
    "Hari": 75000,
    "Gita": 40000
}
higher_salaries = {name: salary
                   for name, salary in salaries.items() 
                   if salary >=50000
                   }
print(higher_salaries)
