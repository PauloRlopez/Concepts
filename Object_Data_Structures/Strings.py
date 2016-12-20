
# ------------------------------------------------------------------
#	Strings in python are kept as sequences. Everthing in python
#	strings are stored as sequences and thus we can use something call
#	indexing or slicing....indexing in python starts at 0! 
# ------------------------------------------------------------------


# playing with strings 

# name a string
p = 'This is the letter p!'

print(p)

# Doing indexing 

# grab everything but skip the first letter, in this case 0
print(p[1:]) 

# grab everything but skip the first two letters
print(p[2::])

# grab everything but the last letter
print(p[:-1])

# grab the first element
print(p[0])

# grab the second element 
print(p[1])

# grab all of it but in steps of 2
print(p[::2])

# grab everything and print backwards
print(p[::-1])

# concanating strings 

all = p + ' which is the first letter of my name!'

print(all)

# multiply all by 7

print(all * 7)

# Doing  some Built-in string methods which are used after a period

# our first method is the upper case
print(p.upper())

# splitting by the letter e

print(p.split('e'))

# output 

"""

This is the letter p!
his is the letter p!
is is the letter p!
This is the letter p
T
h
Ti stelte !
!p rettel eht si sihT
This is the letter p! which is the first letter of my name!
This is the letter p! which is the first letter of my name!This is the letter p! which is the first letter of my name!This is the letter p! which is the first letter of my name!This is the letter p! which is the first letter of my name!This is the letter p! which is the first letter of my name!This is the letter p! which is the first letter of my name!This is the letter p! which is the first letter of my name!
THIS IS THE LETTER P!
['This is th', ' l', 'tt', 'r p!']

"""


# ====end!


