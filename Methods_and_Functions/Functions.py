# =====================================================================
#  These are built in functions already built into it.  
#  https://docs.python.org/3.6/library/functions.html  
#
#  But functions can be created by all called user-defined functions.
#
#  Functions  ==> are a set of organized reusable code use for a single 
#  related action.
#
# ======================================================================

# creating a simple function that will print... 
def my_first_func():
	print("This is my first function in python!")
my_first_func()

# def for a name and greeting afterwards  

def name():
	n = input("What it's your name?: ")
	print("Hi", n,", " "How are you Today?")

name()  # calling it without any argument!

# def squaring 
def sqr(x):
	return x**2
sqr(5)
print(sqr(5))

# a function that will multiply two numbers

def multiply_nums(num1, num2):
	return num1 * num2
multiply_nums(5,7) # it should end here
print(multiply_nums(5,7)) # in order to see it on 


# making a prime checker

import math

def a_prime(num):
	'''
	Checking a number if is prime or not
	'''
	if num % 2 == 0 and num > 2:
		return False
	for i in range(3, int(math.sqrt(num)) + 1, 2):
		if num % i == 0:
			return False
	return True 

a_prime(23)
print(a_prime(23))


# converting temperatures from Celsius to Fahrenheit degrees

def temps(T_in_Fahrenheit):
	"""
	return the temperature in degree celsius
	"""
	return [(T_in_Fahrenheit - 32) * (5.0/9.0)]
for t in (45, 55, 67, 77,85,96, 100,112):
	print(t, "Fahrenheit: ", temps(t), " Celcius")
	print("Here are your conversions!")


# creating a function list
def addme(my_str):
	"""
	adds a list into this function
	"""
	my_str = ('The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized');
	print("Guess what is this?: ", my_str)
	return 
my_str = ('I am from the Bill of rights: The Fourth Amendment!' );
addme(my_str)
print("Here is the answer: ", my_str)


# Example of outputs 


"""
This is my first function in python!
What it's your name?: Paulo
Hi Paulo , How are you Today?
25
35
True
45 Fahrenheit:  [7.222222222222222]  Celcius
Here are your conversions!
55 Fahrenheit:  [12.777777777777779]  Celcius
Here are your conversions!
67 Fahrenheit:  [19.444444444444446]  Celcius
Here are your conversions!
77 Fahrenheit:  [25.0]  Celcius
Here are your conversions!
85 Fahrenheit:  [29.444444444444446]  Celcius
Here are your conversions!
96 Fahrenheit:  [35.55555555555556]  Celcius
Here are your conversions!
100 Fahrenheit:  [37.77777777777778]  Celcius
Here are your conversions!
112 Fahrenheit:  [44.44444444444444]  Celcius
Here are your conversions!
Guess what is this?:  The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized
Here is the answer:  I am from the Bill of rights: The Fourth Amendment!

"""
# ==== end!
