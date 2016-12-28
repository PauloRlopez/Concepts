
# This is a class named "Vehicle" that we will use it to inherit it on 
# other classes


class Vehicle:
	def __init__(self, make, engine):
		self.make = make 
		self.engine = engine
		print("The vehicle it's a {}! and the engine size it's of {} cylinders!".format(self.make, self.engine))

class Car(Vehicle):
	def print(self, make, engine):
		Car.__init__(self, make, engine)

class Van(Vehicle):
	def print(self, make, engine):
		Van.__init__(self, make, engine)

class Motorcycle(Vehicle):
	def print(self, make, engine):
		Motorcycle.__init__(self, make, engine)



# creating objects 
# creating cars 

c1 = Car('FERRARI TESTAROSSA', 12)

c2 = Car('FORD MUSTANG GT', 8)

C3 = Car("LAMBORGHINI COUNTACH", 18)

# creating vans

v1 = Van('TOYOTA SIENNA', 6)

v2 = Van('CHRYSLER SEBRING', 6)		

v3 = Van('FORD AEROSTAR', 6)

# creating motorcyles

m1 = Motorcycle('KAWASAKI NINJA H2R', 4)

m2 = Motorcycle('DUCATI 1098S', 2)

m3 = Motorcycle('MV AUGUSTA F4 1000R', 4)


# output 


"""
The vehicle it's a FERRARI TESTAROSSA! and the engine size it's of 12 cylinders!
The vehicle it's a FORD MUSTANG GT! and the engine size it's of 8 cylinders!
The vehicle it's a LAMBORGHINI COUNTACH! and the engine size it's of 18 cylinders!
The vehicle it's a TOYOTA SIENNA! and the engine size it's of 6 cylinders!
The vehicle it's a CHRYSLER SEBRING! and the engine size it's of 6 cylinders!
The vehicle it's a FORD AEROSTAR! and the engine size it's of 6 cylinders!
The vehicle it's a KAWASAKI NINJA H2R! and the engine size it's of 4 cylinders!
The vehicle it's a DUCATI 1098S! and the engine size it's of 2 cylinders!
The vehicle it's a MV AUGUSTA F4 1000R! and the engine size it's of 4 cylinders!


"""

# ====== end!

