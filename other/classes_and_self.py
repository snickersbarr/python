#!/usr/bin/python

class className:
	def createName(self,name):
		self.name=name
	def displayName(self):
		return self.name
	def saying(self):
		print "hello %s" % self.name

# Create objects to refer to class
first = className()
second = className()

# Use methods within objects to assign values
first.createName('Kunal')
second.createName('Pamani')

# Calls displayName method on objects created
print first.displayName()
print second.displayName()

# Saying method does it for you
first.saying()
second.saying()