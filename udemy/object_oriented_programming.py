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
	def __init__(self,breed,name,fur=True): # special method, initiates all attributes of class
		self.breed = breed # characteristics
		self.name = name
		self.fur = fur # By default, set to true

sam = Dog(breed='Lab', name='Sammy')
print sam
print sam.breed
print sam.species
print sam.name
print sam.fur

## Class, object attributes and methods ##
print '## Another Example of Classes ##'
class Circle(object):
	# class object attributes
	pi = 3.14
	
	def __init__(self,radius=1):
		self.radius = radius
	
	def area(self):
		return (self.radius**2) * Circle.pi
	
	def set_radius(self,new_radius):
		self.radius = new_radius
	
	def get_radius(self):
		return self.radius
		
c = Circle(radius = 100)

print c.pi
print c.area()
print c.radius

d = Circle(radius = 10)
print d.radius
c.set_radius(3)
print c.radius
print c.get_radius()

print '## Another Example of Classes ##'
class Animal(object):
	def __init__(self):
		print "Animal Created"
	def whoAmI(self):
		print "Animal"
	def eat(self):
		print "Eating"

a = Animal()

print '## Another Example of Classes (Inheritance)##'
class Dog(Animal):
	def __init__(self):
		Animal.__init__(self)
		print "Dog created"
	def whoAmI(self):
		print "Dog"
	def bark(self):
		print "Woof"

d = Dog()
d.whoAmI()
d.eat() # Can use eat method from inherited class (Animal)

l = [1,2,3]
print l

print '## Another Example of Classes ##'
class Book(object):
	def __init__(self,title,author,pages):
		print "A book has been created!"
		self.title = title
		self.author = author
		self.pages = pages
	
	def __str__(self):
		return "Title: %s, Author: %s, pages %s " %(self.title,self.author,self.pages)
		
	def __len__(self):
		return self.pages
	
	def __del__(self):
		print "A book is gone!"
		
b = Book('Python','Kunal',101)
print b.title
print b.author
print b.pages
print b
print len(b) # Will return the number of pages
del b
# b.title #This wont work now because of the __del__ function