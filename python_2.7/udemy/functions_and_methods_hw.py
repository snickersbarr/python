#!/usr/bin/python

# Volume of a sphere if given a radius
def vol(rad):
	return (4.0/3)*(3.14)*(rad**3)
print vol(3)

# Checks whether a number is in a given range (Inclusive of high and low)
def ran_check(num,low,high):
	if num in range(low,high+1):
		print "%s is in the range" %str(num)
	else:
		print "The number is outside of the range."

ran_check(5,3,10)
ran_check(50,3,10)

# Check the same as above, return a boolean value
def ran_bool(num,low,high):
	return num in range(low,high+1)
print ran_bool(3,1,20)
print ""

# accepts a string and calculate the number of upper case letters and lower case letters
print "Accepts given string and calculates number of upper and lower case letters"
s = 'Hello Mr. Rogers, how are you this fine Tuesday?'

def up_low(s):
	d = {"upper":0, "lower":0}
	for c in s:
		if c.isupper():
			d["upper"]+=1
		elif c.islower():
			d["lower"]+=1
		else:
			pass
	print "Original String: ", s
	print "No. of Upper case character : ", d["upper"]
	print "No. of Lower case characters : ", d["lower"]

up_low(s)
print ""

# Write a Python function that takes a list and returns a new list with unique elements of the first list.
print "Takes a list and returns a new list with unique elements of the first list."
def unique_list(l):
	x = []
	for a in l:
		if a not in x:
			x.append(a)
	return x

print unique_list([1,1,1,1,2,2,3,3,3,3,4,5])
print ""

# Write a Python function to multiply all the numbers in a list.
print "Multiply all the numbers in a list"
def multiply(numbers):
	total = 1
	for x in numbers:
		total *= x
	return total

print multiply([1,3,4])

# Write a Python function that checks whether a passed string is a palindrome or not.
print "Checks whether a passed string is a palindrome or not:"
def palindrome(s):
	s = s.replace(' ','')
	return s == s[::-1]

print palindrome('helleh')
print palindrome('race car')
print palindrome('hello')

# Write a Python function to check whether a string is pangram or not
print "Function to check whether a string is a pangram or not:"
import string

def ispangram(str1, alphabet=string.ascii_lowercase):
	alphaset = set(alphabet)
	return alphaset <= set(str1.lower())

print ispangram("The quick brown fox jumps over the lazy dog")
print ispangram("This is a test to see if my pangram function works")