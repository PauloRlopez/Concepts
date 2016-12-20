#
#  for loops are iterations or repetititons of the same code
#   over and over again
#
#


# creating a for loop which will run for a fixed amount of time

for x in range(0,10):
	print("We're on time %d" % (x)) 
	
# While loops run forever!! but we will put a early exit == break

x = 10

while True:
    print ("Can we get to inifinity?, on %d now!" % (x))
    x += 1
    if x == 20:
    	break  # don't want to diplayed to infinity

# Nested loops are loops that you can run x number of times 
# then code within that code you can run y number of times
# xrange generates them as needed


"""
for x in xrange(1, 10):
	for y in xrange(1, 10):
		print('%d * %d = %d' % (x, y, x*y))

"""

# Early exit, is a loop that can be made to exit before its finished
# by using the break key word


# for else

# strings

string = "Hello, how are you today?"

for s in string:
	print(s)

# List as iterable

list = [1,2,3,4,5,6,7,'We', 'will', 'print', 'this', 'list']

for l in list:
	print(l)

# lists of lists

a_list_in_a_list = [['x', 'y', 'z'], [1, 2, 3], [4, 5, 6]]


for list in a_list_in_a_list:
	for x in list:
		print(x)


# using items()


a_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

for k, v in a_dict.items():	# k for keys & v for values
	print(k)
	print(v)

# output 


"""We're on time 0
We're on time 1
We're on time 2
We're on time 3
We're on time 4
We're on time 5
We're on time 6
We're on time 7
We're on time 8
We're on time 9
Can we get to inifinity?, on 10 now!
Can we get to inifinity?, on 11 now!
Can we get to inifinity?, on 12 now!
Can we get to inifinity?, on 13 now!
Can we get to inifinity?, on 14 now!
Can we get to inifinity?, on 15 now!
Can we get to inifinity?, on 16 now!
Can we get to inifinity?, on 17 now!
Can we get to inifinity?, on 18 now!
Can we get to inifinity?, on 19 now!
H
e
l
l
o
,
 
h
o
w
 
a
r
e
 
y
o
u
 
t
o
d
a
y
?
1
2
3
4
5
6
7
We
will
print
this
list
x
y
z
1
2
3
4
5
6
a
1
b
2
c
3
d


"""


# ======= end!




