#!/usr/bin/python

## Lambda Expressions ##

# create anonymous functions
# usually a one line expression

# simple square root function to square a given number
def square(num):
	result = num**2
	return result
print square(2)
print square(4)

print '-----------------------'

# one line expression of function above
def square(num): return num**2
print square(3)

print '-----------------------'

# even more condensed version of one line expression above
lambda num: num**2
print lambda num: num**2

print '-----------------------'

square2 = lambda num: num**2
print square(5)

# checks for even numbers with modulo 2
even = lambda num: num%2 == 0
print even(10)

# same function with def 
def even(num):
	return num%2 == 0
print even(13)

# Grabs the first character of a string
first = lambda s: s[0]
print first('hello')

# Reverse a string
rev = lambda s: s[::-1]
print rev('hello')


# Adds to arguments together
def adder(x,y):
	return x+y
print adder(10,12)

# Does the same thing
adder2 = lambda x,y: x+y
print adder2(10,12)

# map() filter() reduce()
# These functions work well with lambda
