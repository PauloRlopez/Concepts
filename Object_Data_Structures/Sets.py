



# creating a set with the set() function
# sets are unordered and unique and they only take one
# argument at a time


p = set()

# p.add('one', 1, 'two', 2)

p.add('one')

print(p)

p.add(1)

print(p)

p.add('two')

p.add(2)

print(p)

# can also create a set like this

a_set = set([1,1,2,2,3, 3, 'yes', 'no', 'etc'])

print(a_set)

# gathering the unique set values from a list

list = ['one', 'one', 'one', 'two', 'two', 'three', 'four', 'five', 'five', 'six', 3,3, 
		4,5,5,5,6,7,7,7,8,]

# give me all the unique values
print(set(list))


# output

"""
{'one'}
{1, 'one'}
{'two', 1, 2, 'one'}
{1, 2, 3, 'no', 'etc', 'yes'}
{'two', 'five', 3, 4, 5, 6, 7, 8, 'six', 'four', 'one', 'three'}

"""

# ===end!
