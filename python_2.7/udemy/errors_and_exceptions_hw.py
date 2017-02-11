#!/usr/bin/python

# Problem 1: Handle the exception throw by the code below using try and except blocks
# for i in ['a', 'b', 'c']:
# 	print i**2

# Answer
for i in ['a', 'b', 'c']:
	try:
		print i**2
	except TypeError:
		print "There is a type error"
		
# Problem 2: Handle the exception thrown and then print 'All Done'

#x = 5
#y = 0
#
#z = x/y

# Answer

x = 5
y = 0

try:
	z = x/y
except:
	print "You can't divide by zero!"
finally:
	print "All Done"
	
# Problem 3: Write a function that asks for an integer and prints the square of it

# Answer

def ask():
	while True:
		try:
			val = int(raw_input("Please enter an integer: "))
		except:
			print "Looks like you did not enter an integer"
			continue
		else:
			val = val**2
			break
	print "Thank you, your number squared is: {0}".format(val)
			
ask()

