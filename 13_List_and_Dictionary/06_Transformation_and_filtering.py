salaries = [25000, 45000, 60000, 75000, 40000, 90000]
higher_salaries_increasement  = [salary*1.10
                                 for salary in salaries 
                                 if salary >= 50000
                                ]
print(higher_salaries_increasement)