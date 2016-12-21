#  ------------------------------------------------------------ # 
#   While loops: will run until a condition is met
# -------------------------------------------------------------- # 




# constructing my first while loop with an else statement
# if given 12 the while loop will stop until the condition is met of p < 21
p = 12

while p < 21:
	print('p is currently: ', p)  
	print('p is still less than 21, adding 1 to p')
	p+=1

else:
	print('You have reached your destination!')

#  another while loop but this time with break statement

p = 0

while p < 7:
	print('p is currently: ', p)
	print('p is still less than 7, continue to add 1 to p')
	p+=1
	if p == 5:
		print('I need to take a break here because p has reached 5')
	else:
		print('I need to continue adding to p')
		continue
	
# break statement

count = 1

while (count): 
	print('Given count is really true!')
	break  # don't want this count to forever
print("Good bye!")

# string break statement

p = 'Programming'

for letter in p:
	if letter == 'i':
		break
	print('The current leter is:', letter) 


# pass statement

var = 7

while var > 0:
	print('The current variable value is:', var)
	var = var -1
	if var == 4:
		break
print('Stop, see you later!')

# output

"""

p is currently:  12
p is still less than 21, adding 1 to p
p is currently:  13
p is still less than 21, adding 1 to p
p is currently:  14
p is still less than 21, adding 1 to p
p is currently:  15
p is still less than 21, adding 1 to p
p is currently:  16
p is still less than 21, adding 1 to p
p is currently:  17
p is still less than 21, adding 1 to p
p is currently:  18
p is still less than 21, adding 1 to p
p is currently:  19
p is still less than 21, adding 1 to p
p is currently:  20
p is still less than 21, adding 1 to p
You have reached your destination!
p is currently:  0
p is still less than 7, continue to add 1 to p
I need to continue adding to p
p is currently:  1
p is still less than 7, continue to add 1 to p
I need to continue adding to p
p is currently:  2
p is still less than 7, continue to add 1 to p
I need to continue adding to p
p is currently:  3
p is still less than 7, continue to add 1 to p
I need to continue adding to p
p is currently:  4
p is still less than 7, continue to add 1 to p
I need to take a break here because p has reached 5
p is currently:  5
p is still less than 7, continue to add 1 to p
I need to continue adding to p
p is currently:  6
p is still less than 7, continue to add 1 to p
I need to continue adding to p
Given count is really true!
The current leter is: P
The current leter is: r
The current leter is: o
The current leter is: g
The current leter is: r
The current leter is: a
The current leter is: m
The current leter is: m
The current variable value is: 7
The current variable value is: 6
The current variable value is: 5
Stop, see you later!

"""

# === end!





