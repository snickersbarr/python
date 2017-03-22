#!/usr/bin/python

### Exercise 21 ###
### Functions Can Return Something ###

def add(a, b):
	print "Adding %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b


print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anway
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what , "Can you do it by hand"

# Study Drills #
# Dummy Formula: (24 + 34 / 100 - 1023)
# Expected result: -998.66

# This is a failed attempt, come back to it

number_1 = 24
number_2 = 34
number_3 = 100
number_4 = 1023

which = add(number_1, ddivide(number_2, subtract(number_3, number_4))
print which