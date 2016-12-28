# creating a simple class

class Person(object):
	"""docstring for Person"""
	# constructor function
	def __init__(self, name, age):
		self.name = name
		self.age = age
		print("If your name is {}, then your age must be {}!".format(name, age))
		
# creating objects 

p1 = Person('Albert Einstein', 138)
p2 = Person('Isaac Newton',375)

# outcome

"""
If your name is Albert Einstein, then your age must be 138!
If your name is Isaac Newton, then your age must be 375!

"""

# ==== end!

