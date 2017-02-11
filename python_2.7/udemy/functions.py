#!/usr/bin/python

## Functions ##
# Useful device that groups together a set of statements so they can be run more than once.
# Specify parameters that can serve as inputs to the functions


def first_function(arg1,arg2):
	print arg1+arg2
	'''
	Here is my docstring
	'''
first_function(1, 2)

def say_hello():
	print "hello "
say_hello()

def greeting(name):
	print "Hello " + name
greeting('Kunal')

print '----------------------------'

def add_num(num1,num2):
	return num1+num2
x = add_num(3, 4)
print x	

print '----------------------------'

# can pass either int or string as arguments
def add_num(num1,num2):
	return num1+num2
x = add_num('one', 'two')
print x	

"""
This function checks for prime numbers
INPUT: A number
OUTPUT: A print statement whether or not the number is prime
"""
def is_prime(num):
	for n in range(2,num):
		if num % n == 0:
			print 'Not Prime'
			break
	else:
		print 'The number is prime'
is_prime(13)
is_prime(12)