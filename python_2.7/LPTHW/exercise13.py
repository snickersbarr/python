#!/usr/bin/python

### Exercise 13 ###
### Paramters, Unpacking, Variables ###

from sys import argv

script, first, second, third = argv
# HW
fourth = raw_input("Please enter a fourth variable: ")

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "Your fourth variable is:", fourth


# When running this, you would run python exercise13.py (variable1, variable2, variable3)
# Can replace first, second, third with whatever you want when running the program