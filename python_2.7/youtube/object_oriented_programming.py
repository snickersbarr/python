#!/usr/bin/python

class exampleClass: # Class
	eyes="blue"
	age=22
	def thisMethod(self):
		return 'hey this method worked'


# Will just tell you the class was created
print exampleClass

# first step is to create an object
# can then use this object to get data out of class

exampleObject=exampleClass()

print exampleObject.eyes
print exampleObject.age
print exampleObject.thisMethod()

print 'Break'
print '\n'
# Classes and Self #

# any function in a class is now a method
# methods in a class must always take the first paramater of (self)
class className:
	def