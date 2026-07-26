'''
List is Mutable 
Question number 1
Create a list called cities with these items:
    Pokhara
    Kathmandu
    Chitwan
    Butwal
Then:
    Print the whole list.
Change "Chitwan" to "Biratnagar".
Print the updated list.
'''
cities = ["Pokhara", "Kathmandu", "Chitwan", "Butwal"]
print(f"Some Cities from Nepal are: {cities}")

cities[2] = "Biratnagar"   # since list is mutable we can change the value of list. Chitwan lies in index 2 and it was replaced by Biratnagar
print(f"Some Cities after modify are: {cities}")