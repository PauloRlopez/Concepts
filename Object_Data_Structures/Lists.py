#
#  List are created in a sequence order just like strings, So
#  We can removed or add objects from the list or sequence...
#  

# creating a list as a variable


this_is_a_list = [0,1,2,3,4,5,6,7,]

print(this_is_a_list)

# checking the lenght of this list
print(len(this_is_a_list))

# creating a list with numbers and strings 

another_list = [ 'This list consist of:', 0,1,2,3]

print(len(another_list))
print(another_list)

# we can also slice and do some index on this list as with strings

print(another_list[1:])

# Adding  another string

more_list = another_list + ['zero, one, two, three']

print(more_list)

# Using append to add objects to the list

simple_list = ['4','5','6','7']

print(simple_list)

new = simple_list.append('Hi')

print(new)


revs = simple_list.reverse()

print(revs)

# creating a nested list (data within data)

a = [1,2,3,4]
b = [5,6,7,8]
c = [9,10,11,12]

a_nest = [a, b, c]
print(a_nest)  # here is our nested list

# we can also slice it, index it, yet there are two levels 
# the items in the nested list and the items of a,b & c

print(a_nest[1])

print(a_nest[0][1])

# getting the number 7

print(a_nest[1][2])

# using list comprehensions 

# for every row in a_nest grab the element 1
second_col = [row[1]for row in a_nest]

print(second_col)


#  output 
"""
[0, 1, 2, 3, 4, 5, 6, 7]
8
5
['This list consist of:', 0, 1, 2, 3]
[0, 1, 2, 3]
['This list consist of:', 0, 1, 2, 3, 'zero, one, two, three']
['4', '5', '6', '7']
None
None
[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
[5, 6, 7, 8]
2
7
[2, 6, 10]

"""

# ==end!















