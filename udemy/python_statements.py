#!/usr/bin/python


# reassigning values to variables through if statement
a = 5
b = 1


# end of a line is the end of statement, other languages might requires symbols to define the end of a line
if a > b:
	a = 2 # uses indendation and whitespace to define statements and nested statements
	b = 4
	
print a
print b

# example if and else statements:
if True:
	print 'It is True'
	
x = False
if x:
	print 'x is True'
else:
	print 'I will print when x is anything not True'

x = True
if x:
	print 'x is True'
else:
	print 'I will print when x is anything not True'

# example if, elif, else statement
loc = 'Bank'
if loc == 'Auto Shop':
	print 'Welcome to the Auto Shop'
elif loc == 'Bank':
	print 'Welcome to the Bank'
elif loc == 'Mall':
	print 'Welcome to the Mall'
else:
	print 'Where are you?'


person = 'Sam'
if person == 'Sam':
	print 'Hi Sam!'
else:
	print "What's your name?" #need double quotes due to string using single quote

