#!/usr/bin/python

l = [1,2,3]
print l.count(2)

## Objects ##
## Everything is an object ##
## Use type function to check type of object ##

print type(1)
print type([1,2,3])
print type({2:3})

def square(num):
	return num**2
print type(square)

## Classes ##
## Allows you to create your own objects ##
# By convention, class names are capitalized, unlike functions which are lowercase
class Sample(object):
	pass

# Instance of Sample class
# Instantiating Sample class

X = Sample()
print type(X)

## Can define class attributes and methods ##
## An atribute is a characteristic of an object. A method is an operation we can perform with the object ##

class Dog(object):
	species = 'mammal' # Class Object Attribute
	def __init__(self,breed): # special method
		self.breed = breed # characteristics

sam = Dog(breed='Lab')
print sam
print sam.breed