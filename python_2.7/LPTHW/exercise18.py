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
	print "arg1L %r" % arg1

