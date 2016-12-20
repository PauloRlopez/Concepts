#
#  In Python just like in a language a word can be map to a 
#  to a meaning.  In python dicitonaries keys are map (words)
#  to value (meanings)
#


# creating a dictionary 
a_dict = {'a': 'one', 'b': 'two', 'c': 'three'}
print(a_dict)

# using the key value to gather the dictionary information 
# we cannot use a_dict[0] it will not work!
print(a_dict['b'])

number_dict = {'one': 1, 'two': 2, 'three': 3}
print(number_dict)

# changing the value of key: 'three'

number_dict['three'] = number_dict['three']  + 4
print(number_dict) # new value for 'three' = 7

# another way of adding
number_dict['one'] += 7  
print(number_dict['one'])

# creating an empty dictionary key by assingments

new_dict = {}

# adding a new value to new_dict
new_dict['word'] = 'hello'

print(new_dict)

# creating nested dictionaries 

nest_dict = {'first': {'two': {'three': 'four'}}}
print(nest_dict)

# finding the four value in the nest_dict

print(nest_dict['first']['two']['three']) 

# can also change all to upper or lower case 

# getting the key values

print(number_dict.keys())
print(number_dict.values())  # out of order because we can call them by keys


print(number_dict.items())  # a tuples of items

# output
"""

{'a': 'one', 'c': 'three', 'b': 'two'}
two
{'three': 3, 'two': 2, 'one': 1}
{'three': 7, 'two': 2, 'one': 1}
8
{'word': 'hello'}
{'first': {'two': {'three': 'four'}}}
four
dict_keys(['three', 'two', 'one'])
dict_values([7, 2, 8])
dict_items([('three', 7), ('two', 2), ('one', 8)])

"""

#===end!



