# creating a password program

password = "Hello"

for i in range(3):
	pwd = input("Enter password: ")
	j = 2
	if(pwd == password):
		print("Welcome")
		break
	else:
		print("Wrong password, chances left: ", j-i) # 3 times
		continue
    
#print("Try to remember and try next time.")


"""

If inputing the password correctly:

Enter password: Hello
Welcome

"""

"""
If inputting the wrong password:

Enter password: hi
Wrong password, chances left:  2
Enter password: hola
Wrong password, chances left:  1
Enter password: chau
Wrong password, chances left:  0


"""

# ====== end!
