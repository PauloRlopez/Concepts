#
#  Tuples do not support item assignment
#   they are immutable
#
#

# a tuple has parenthesis 

tup = (1,2,3,4,5,6,7)

# can check the length

print(len(tup))

# it also has slicing

print(tup[-2])

# there are only two methods count and index

# we can check the index of 1
print(tup.index(1))

# this count the number of time s the variable appears
print(tup.count(1))


# but we cannot reassign 

# tuples are great when don't want a program to be changed

# but you can put lists inside tuples???


tup2 = ('one', 'two', [1, 2])

print(tup2)  # ('one', 'two', [1, 2])s

# we are allowed to modify the internal list as

a = [1,2,3]
b = [4,5,6]
tup3 = (a, b)
print(tup3)

tup3[0][1] = 7 # grabbing the tuple 'a' @ 2nd position
print(tup3) # with variables changed


# output

"""
7
6
0
1
('one', 'two', [1, 2])
([1, 2, 3], [4, 5, 6])
([1, 7, 3], [4, 5, 6])

"""

# ==end!



