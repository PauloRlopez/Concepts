
# 
class Person(object):
	"""docstring for Person"""
	# constructor function
	def __init__(self, name):
		self.name = name
		self.attend = 0
		self.grades = []

		print("Welcome {}".format(name))

	def addgrades(self, grades):
		self.grades.append(grades)

	def attenddays(self):
		self.attend += 1

	def getavg(self):
		return sum(self.grades) / len(self.grades)
		
		
		
# creating objects 

p1 = Person("Albert")
print("Your attendance is: ", p1.attend)
p1.attenddays()
print("Your attendance is: ", p1.attend)

p1.grades
p1.addgrades(99)
p1.addgrades(98)
p1.addgrades(90)
p1.addgrades(88)
p1.addgrades(100)

print(p1.name, "," ,"These are your grades: ", p1.grades)
print("Here are you grade averages: ", p1.getavg())
print("Great Job!")


# output 


"""
Welcome Albert
Your attendance is:  0
Your attendance is:  1
Albert , These are your grades:  [99, 98, 90, 88, 100]
Here are you grade averages:  95.0
Great Job!


"""

# ===== end!









