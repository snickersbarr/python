#!/usr/bin/python

# Volume of a sphere if given a radius
def vol(rad):
	return (4.0/3)*(3.14)*(rad**3)
print vol(3)

# Checks whether a number is in a given range (Inclusive of high and low)
def ran_check(num,low,high):
	if num in range(low,high+1):
		print "%s is in the range" %str(num)
	else:
		print "The number is outside of the range."

ran_check(5,3,10)
ran_check(50,3,10)
