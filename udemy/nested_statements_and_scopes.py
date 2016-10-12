#!/usr/bin/python

x = 25

def printer():
	x = 50
	return x

print x #global variable
print printer() #local variable to printer()

# LEGB Rule
# L:Local Names assigned in any way within a function (def or lambda)), and not declared global in that function.

# E: Enclosing function locals - Name in the local scope of any and all enclosing functions (def or lambda), from inner to outer.

# G: Global (module) - Names assigned at the top-level of a module file, or declared global in a def within the file.

# B: Built-in (Python) - Names preassigned in the built-in names module : open,range,SyntaxError,...

name = 'This is a global name'

def greet():
	# Enclosing function
	name = 'Sammy'
	
	def hello():
		print 'Hello '+name
	hello()

greet()

print name

print '----Another Example----'
x = 50

def func(x):
	print 'x is', x
	x = 2
	print 'Change local x to', x
	
func(x)
print 'x is still', x

print '----Another Example----'

def func():
	global x
	print 'This function is now using the global x!'
	print 'Because of global, x is: ', x
	x = 2
	print 'Ran func(), changed global x to', x

print 'Before calling func(), x is: ', x
func()
print 'Value of x (outside of func()) is :', x

# use globals() and locals() functions to check what are your current local and global variables

