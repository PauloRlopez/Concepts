
# opening the text file

file = open('history.txt')

# have to put read because I'm not on jupyter
# reading the file..
print(file.read())

# tell the file to go back to the beginning of the file
#file.seek(0)

# can also read the file by using readlines
#print(file.readlines())

# writing to the file with w+ function
f = open('history.txt', 'w+')

f.write('History is exciting!')

# an iteration/ for loop also can open the file

for lines in open('history.txt'):
	print(lines)

# output

#After open the original content,
#then we wrote on the file this:

"""
History is exciting!

"""

# ===end!

