#!/usr/bin/python

#### String Concatenation and Replication ####

alicebob = 'Alice' + 'Bob'
print alicebob

# Output is alicebob because + operator concatenates two strings

'''
# Example Error:

alice42 = 'Alice' + 42

AliceBob
Traceback (most recent call last):
  File "chapter1.py", line 10, in <module>
	alic42 = 'Alice' + 42
TypeError: cannot concatenate 'str' and 'int' objects

'''

# String replicator using * :

threeAlices = 'Alice ' * 3
print threeAlices

#### Variables ####
# Already did this above, but example for assignign variables:
spam = 42
print spam

eggs = 20

# This will print the sum of the two values assigned to the variables being used
print spam + eggs

spam = spam + 10
print spam

# Reassigning variable to a string. Python will forget the old variable here and print whatever is the most recent assignment
spam = 'Hello'
print spam

spam = 'Goodbye'
print spam

# Assigning a value to a variable is called initialization

'''
Rules for Variable Names:

1. It can be only one word
2. It can use only letters, numbers, and the underscore (_) character.
3. It can't begin with a number

Other things about variables:

1. Variable names are case-sensitive :
	Examples:
		spam
		Spam
		SPaM
		sPam

		All of these are different variables

