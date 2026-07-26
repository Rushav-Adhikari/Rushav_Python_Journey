'''
Write the code for this:
    books = ["Python", "SQL", "Excel", "Power BI"]
Now:
    Print the original list.
    Use pop() without an index.
    Store the removed item in a variable called removed_book.
    Print the removed book.
    Print the updated list.
'''
books = ["Python", "SQL", "Excel", "Power BI"]
print(f"Original List: {books}")
removed_book = books.pop()
print(f"Removed Book: {removed_book}")
print(f"Updated List: {books}")
print(books.pop())
