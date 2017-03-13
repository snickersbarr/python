#!/usr/bin/python

### Exercise 18 ###
### Names, Variables, Code, Functions ###

def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# *args is pointless. Another way:
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# This just takes one argument:
def print_one(arg1):
	print "arg1 %r" % arg1

# This takes no arguments
def print_none():
	print "I got nothin'"


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()