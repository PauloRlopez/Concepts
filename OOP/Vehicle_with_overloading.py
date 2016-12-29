

# This is a class named "Vehicle" that we will use it to inherit it on 
# other classes but with overloading now


class Vehicle:
	def __init__(self, make, engine):
		self.make = make 
		self.engine = engine
	def __str__(self):
		return("make: {}\nengine:{}\n".format(self.make, self.engine))

class Car(Vehicle):
	def __init__(self, make, engine, type):
		Vehicle.__init__(self, make, engine)
		self.type = type
	def __str__(self):
		return(Vehicle.__str__(self)+"type: {}".format(self.type))


class Van(Vehicle):
	def __init__(self, make, engine, type):
		Vehicle.__init__(self, make, engine)
		self.type = type
	def __str__(self):
		return(Vehicle.__str__(self)+"type: {}".format(self.type))

class Motorcycle(Vehicle):
	def __init__(self, make, engine, type):
		Vehicle.__init__(self, make, engine)
		self.type = type
	def __str__(self):
		return(Vehicle.__str__(self)+"type: {}".format(self.type))



# creating objects 
# creating cars 

c1 = Car('FERRARI TESTAROSSA', 12, 'sports')
print(c1)
c2 = Car('FORD MUSTANG GT', 8, 'muscle car')
print(c2)
c3 = Car("LAMBORGHINI COUNTACH", 18, 'sports')
print(c3)
# creating vans

v1 = Van('TOYOTA SIENNA', 6, 'family van')
print(v1)
v2 = Van('CHRYSLER SEBRING', 6, 'family van')		
print(v2)
v3 = Van('FORD AEROSTAR', 6, 'family van')
print(v3)
# creating motorcyles

m1 = Motorcycle('KAWASAKI NINJA H2R', 4, 'moto-race')
print(m1)
m2 = Motorcycle('DUCATI 1098S', 2, 'moto-race')
print(m2)

m3 = Motorcycle('MV AUGUSTA F4 1000R', 4, 'moto-race')
print(m3)

# output

"""

make: FERRARI TESTAROSSA
engine:12
type: sports
make: FORD MUSTANG GT
engine:8
type: muscle car
make: LAMBORGHINI COUNTACH
engine:18
type: sports
make: TOYOTA SIENNA
engine:6
type: family van
make: CHRYSLER SEBRING
engine:6
type: family van
make: FORD AEROSTAR
engine:6
type: family van
make: KAWASAKI NINJA H2R
engine:4
type: moto-race
make: DUCATI 1098S
engine:2
type: moto-race
make: MV AUGUSTA F4 1000R
engine:4


"""

# ========== end!





