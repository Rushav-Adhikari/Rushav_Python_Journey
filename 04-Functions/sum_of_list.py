'''
5. Sum of List

Create a function that:

takes a list of numbers
returns total sum

👉 Example: [1,2,3] → 6
'''

def sum_list(lst):
    return sum(lst)

lst = [1,2,3]
lst_sum = sum_list(lst)
print(f"The sum of the list is {lst_sum}")