#!/usr/bin/python

## List Comprehensions ##

# building list out from string with append method
l = []
for letter in 'word':
	l.append(letter)
print l

# one line for loop built inside of brackets
# will do the same thing in a single line
l = [letter for letter in 'word']
print l

# x^2 : in {0,1,2,..10}
#x^2 for x in range(0,11)

# print ever thing squared from 0-10
lst = [x**2 for x in range(0,11)]
print lst

# prints even numbers 0-10
lst = [number for number in range(11) if number % 2 == 0]
print lst

print '------------------------------------------'

# does the same thing but with a for loop and if statement separated line by line
lst = []
for number in range(11):
	if number %2 == 0:
		lst.append(number)
print lst

# prints for ever even number
print '------------------------------------------'
lst = []
for number in range(11):
	if number %2 == 0:
		lst.append(number)
		print lst

# prints for every number
print '------------------------------------------'
lst = []
for number in range(11):
	if number %2 == 0:
		lst.append(number)
	print lst

print '------------------------------------------'	

celsius = [0,10,20.1,34.5]

# converting celsius to fahrenheit
# using 5.0 to make sure there are no floating point errors
fahrenheit = [(temp * (9/5.0) + 32) for temp in celsius]
print fahrenheit

print '------------------------------------------'	

# same in for loop
celsius = [0,10,20.1,34.5]
fahrenheit =[]
for temp in celsius:
	fahrenheit.append(temp * (9/5.0) + 32)
print fahrenheit

print '------------------------------------------'	

lst = [x**2 for x in range(11)]
print lst

print '------------------------------------------'	
# printing out everything to the fourht power now with nested list comprehensions
lst = [x**2 for x in [x**2 for x in range(11)]]
print lst
