# tup = 4,5,6 # or can be written as tup = (4,5,6)
# print(tup) # prints (4, 5, 6)


# # to change the value of any list into the tuple

# lis = [1, 2, 3]
# tup1 = tuple(lis)
# print(tup1) # prints (1, 2, 3)
# print(type(tup1)) # prints <class 'tuple'>

# # to change the value of any string into the tuple

# str1 = "Rushav"
# tup2 = tuple(str1)
# print(tup2) # prints ('R', 'u', 's', 'h', 'a', 'v')
# print(tup2[0]) # prints R
# print(tup2[-1]) # prints v 
# print(tup2[1:4]) # prints ('u', 's', 'h')

# to make a nested tuple

# a = (1, 2, 3), (4, 5, 6)
# print(a) # prints ((1, 2, 3), (4, 5, 6))
# print(a[0]) # prints (1, 2, 3)
# print(a[1]) # prints (4, 5 ,6)

# # object stored in a tuple may be mutable themselves, once the tuple is created, it cannot be changed.
# tup = tuple(["Foo" , [1,2,3], True])
# print(tup) # prints ('Foo', [1, 2, 3], True)
# # tup[2] = False # this will raise an error because tuples are immutable
# tup[1][0] = 100 # this will not raise an error because the list inside the tuple is mutable
# tup[1].append(3) # this will not raise an error because the list inside the tuple is mutable
# print(tup)

# to concatenate two tuples
# a = (1, 2, 3, 4, 5)+ (4, None, "Rushav")
# print(a) # prints (1, 2, 3, 4, 5, 4, None, 'Rushav')
# print(type(a)) # prints <class 'tuple'>

# Multiplying a tuple with an integer will create a new tuple that repeats the original tuple that many times.
# a = (1, 2, 3, 4, 5) * 3
# b = ('a', 'b', 'c') * 2
# c = (1, 2, 3) * 0
# print(a) # prints (1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
# print(b) # prints ('a', 'b', 'c', 'a', 'b', 'c')
# print(c) # prints ()

#  Unpacking the tuples

# tup = (1, 2, 3, 4, 5 , (6, 7, 8))
# a, b, c, d, e, (f,g,h) = tup
# print(a) # prints 1
# print(h)

#  A common use of variable unpacking is iterating over sequences of tuples or lists.

seq = [(1, 2), (3, 4), (5, 6)]
for a, b in seq:
    print(f"a: {a}, b: {b}") # prints First: 1, Second: 2 First: 3, Second: 4 First: 5, Second: 6