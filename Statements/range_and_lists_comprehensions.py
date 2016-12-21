#
# the range() function
# list comprehension:  loops built inside brackets, how cool!
#

# The range function


range(-12,21)

x = range(-12,21)
type(x)
print(x)

# creating a range from -12 to 21

start = -12
stop = 21

for num in range(start, stop):
	print(num)


# list comprehensions

# creating an empty list

l = []

for letter in 'BuenaVistaSocialClub':  # this is an afrocuban musical club....
	l.append(letter)
	print(l) # I like the way this prints 

#  same but notice the print line..... 
for letter in 'BuenaVistaSocialClub':
	l.append(letter)
print(l) # but it should be like this


# another list: same as above with a loop inside the brackets

b = [letter for letter in 'BuenaVistaSocialClub']
print(b)

# same as above but doing a range() functions
# with a loop inside the brackets and with an even count

lst = [number for number in range(100) if number % 2 == 0]
print(lst)

# even numbers in range of 100 with a fourth count!

lst = []

for number in range(100):
	if number % 4 == 0:
		lst.append(number)
print(lst)

# printing  up to 12 numbers with a double multiplication format (doubling it)

xls = [x**2 for x in [x**2 for x in range(12)]]
print(xls)

# output 

"""

range(-12, 21)
-12
-11
-10
-9
-8
-7
-6
-5
-4
-3
-2
-1
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
['B']
['B', 'u']
['B', 'u', 'e']
['B', 'u', 'e', 'n']
['B', 'u', 'e', 'n', 'a']
['B', 'u', 'e', 'n', 'a', 'V']
['B', 'u', 'e', 'n', 'a', 'V', 'i']
['B', 'u', 'e', 'n', 'a', 'V', 'i', 's']
['B', 'u', 'e', 'n', 'a', 'V', 'i', 's', 't']
['B', 'u', 'e', 'n', 'a', 'V', 'i', 's', 't', 'a']
['B', 'u', 'e', 'n', 'a', 'V', 'i', 's', 't', 'a', 'S']
['B', 'u', 'e', 'n', 'a', 'V', 'i', 's', 't', 'a', 'S', 'o']
['B', 'u', 'e', 'n', 'a', 'V', 'i', 's', 't', 'a', 'S', 'o', 'c']
['B', 'u', 'e', 'n', 'a', 'V', 'i', 's', 't', 'a', 'S', 'o', 'c', 'i']
['B', 'u', 'e', 'n', 'a', 'V', 'i', 's', 't', 'a', 'S', 'o', 'c', 'i', 'a']
['B', 'u', 'e', 'n', 'a', 'V', 'i', 's', 't', 'a', 'S', 'o', 'c', 'i', 'a', 'l']
['B', 'u', 'e', 'n', 'a', 'V', 'i', 's', 't', 'a', 'S', 'o', 'c', 'i', 'a', 'l', 'C']
['B', 'u', 'e', 'n', 'a', 'V', 'i', 's', 't', 'a', 'S', 'o', 'c', 'i', 'a', 'l', 'C', 'l']
['B', 'u', 'e', 'n', 'a', 'V', 'i', 's', 't', 'a', 'S', 'o', 'c', 'i', 'a', 'l', 'C', 'l', 'u']
['B', 'u', 'e', 'n', 'a', 'V', 'i', 's', 't', 'a', 'S', 'o', 'c', 'i', 'a', 'l', 'C', 'l', 'u', 'b']
['B', 'u', 'e', 'n', 'a', 'V', 'i', 's', 't', 'a', 'S', 'o', 'c', 'i', 'a', 'l', 'C', 'l', 'u', 'b', 'B', 'u', 'e', 'n', 'a', 'V', 'i', 's', 't', 'a', 'S', 'o', 'c', 'i', 'a', 'l', 'C', 'l', 'u', 'b']
['B', 'u', 'e', 'n', 'a', 'V', 'i', 's', 't', 'a', 'S', 'o', 'c', 'i', 'a', 'l', 'C', 'l', 'u', 'b']
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
[0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96]
[0, 1, 16, 81, 256, 625, 1296, 2401, 4096, 6561, 10000, 14641]

"""

# ====== end!
