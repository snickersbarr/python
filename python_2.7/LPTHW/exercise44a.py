#!/usr/bin/python

### Exercise 44 ###
### Inheritance Versus Composition ###

## Implicit Inheritance ##

class Parent(object):

	def implicit(self):
		print "PARENT implicit()"

# Make a class named Child which inherits from Parent
class Child(Parent):
	pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()