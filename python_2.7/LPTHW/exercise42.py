#!/usr/bin/python

### Exercise 42 ###
### Is-A, Has-A, Objects, and Classes ###

## Animal is-a object(yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

## Dog is-a Animal
class Dog(Animal):

	def __init__(self, name):
		## Dog has-a __init__ that takes self and name parameters.
		self.name = name

## Cat is-a Animal
class Cat(Animal):

	def __init__(self, name):
		## Cat has-a __init__ that takes self and name parameters.
		self.name = name

## Person is-a object
class Person(ojbect):

	def __init__(self, name):
		## Person has-a __init__ that takes self and name parameters.
		self.name = name

		## Person has-a pet of some kind
		self.pet = None

## Employee is-a Person
class Employee(Person):

	def __init__(self, name, salary):
		## Employee has-a __init__ that takes self and name, salary parameters.
		super(Employee, self).__init__(name)
		## From self get the salary attribute and set it to salary
		self.salary = salary

## Fish is-a object
class Fish(object):
	pass

## Salmon is-a Fish
class Salmon(Fish):
	pass

## Halibut is-a Fish
class Halibut(Fish):
	pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## From mary get the pet attribute and set it to satan
mary.pet = satan

## Set frank to an instance of class Employee
frank = Employee("Frank", 120000)

## frank has a pet named rover
frank.pet = rover

## flipper is a Fish
flipper = Fish()

## Set crouise to an instance of class Salmon
crouise = Salmon()

## Set harry to an instance of class Halibut
harry = Halibut()