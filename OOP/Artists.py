
# creating an object named Music

class Music(object):  # this is the class
    # creating the special method:  to initialize the attributes s
    def __init__(self, genre, name, yearBorn):  # this is our methods constructions
        # creating the attributes
        self.genre = genre
        self.name = name
        self.yearBorn = yearBorn
artistOne= Music( genre = 'Classical', name = 'Bethoven', yearBorn=1770 ) # creating instances of the genre class
print(artistOne.genre, ",", artistOne.name, ",", artistOne.yearBorn, ".")  # printing the object


# outcome

"""

Classical , Bethoven , 1770 .

"""

# ===== end!
