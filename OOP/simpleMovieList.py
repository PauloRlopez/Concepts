

# objects with special methods

class Movies(object):
    """ docstring for Movies """
    # initialization
    def __init__(self, title, genre, year):
        self.title = title
        self.genre = genre
        self.year = year
   # creating a special method
    def __str__(self):
        return("Title:  %s, Genre: %s, Year: %s" %(self.title, self.genre, self.year))

# creating objects

movie = Movies('Underworld: Blood Wars', 'Action', '2017')
print(movie)
movie2 = Movies('Mancherster by the Sea', 'Drama', '2017')
print(movie2)


# output

"""

Title:  Underworld: Blood Wars, Genre: Action, Year: 2017
Title:  Mancherster by the Sea, Genre: Drama, Year: 2017

"""

# ===== end!
