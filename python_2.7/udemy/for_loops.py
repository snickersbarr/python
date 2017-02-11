#!/usr/bin/python

"""
Example for for loop:
for item in object:
	statements to do stuff
"""

l = [1,2,3,4,5]
print l


# 'element' is an item that can be named anything in for loops
# prints every item in list
for element in l:
	print element
	
# for every item in for loop, print the string provided
for num in l:
	print 'something!'
	
# MODULO
# Provides the remainder in ZeroDivisionError
# uses % symbol, prints remainder
print 10 % 3
# no remainder
print 4 % 2


# print even numbers
print 'Print Even Numbers:'
for num in l:
	if num % 2 == 0:
		print num
		
# print odd numbers
print 'Print odd Numbers:'
for num in l:
	if num % 2 == 1:
		print num
		
# print even numbers
print 'Print even or odd numbers:'
for num in l:
	if num % 2 == 0:
		print num
	else:
		print 'Odd number!'

print 'List sum:'

# Adds each number to the last starting with 0, or keeping a running tally
list_sum = 0
for num in l:
	list_sum = list_sum + num
print list_sum

# Use += operators to shorten, does the same as for loop above
list_sum = 0
for num in l:
	list_sum += num
print list_sum

s = 'this is a string!'

# prints every item in sequence line by line
for letter in s:
	print letter
	
# another example
tup = (1,2,3,4,5)
for item in tup:
	print item

# tuples inside a list
l = [(2,4),(6,8),(10,12)]
print l
print l[1][0] # prints elements within list then within tuple with []

# prints every element in list
for tup in l:
	print tup
	
# Tuple unpacking, with tuples in a sequence, can access items inside of them
for (t1,t2) in l:
	print t1
print '\n'
	
for (t1,t2) in l:
	print t2
print '\n'

# prints the sum of each tuple in list
for (t1,t2) in l:
	print t1 + t2
print '\n'

# creating a dictionary and prints just the keys
d = {'k1':1,'k2':2,'k3':3}
print d
for item in d:
	print item
print '\n'

# prints keys and values
for k,v in d.iteritems():
	print k
	print v
	
