#!/usr/bin/python
# This module is about error handling. Specifically with try, except, finally blocks and try, except, else blocks as well as all four concepts put to gether


'''
Example:
try:
	2 + 's'
except typeError:
	print "There was a type error!"
'''	

''' 
output:
Traceback (most recent call last):
	  File "errors_and_exceptions.py", line 5, in <module>
		except typeError:
	NameError: name 'typeError' is not defined
'''

# Another Example:
# This example will compile with no error because 'typeError' was not defined above	
try:
	2 + 's'
except:
	print "There was a type error"
finally:
	print "Finally this was printed"

'''
Open a file. If it does not exist, it will write the file because of the 'w'. '''
	
try:
	f = open('testfile1232', 'w') # When opening a file in python, it will just create the file if it does not exist
	# The 'w' tells python that we can write to the file
	f.write('Test write this')
except:
	print 'Error in writing to the file!' # This is why this does not error out when trying to open the file
else:
	print 'File write was a success'

'''
This will cause an error but the program will keep running because we are trying to read a file that does not exist.
'''
	
try:
	f = open('testfile1231', 'r') # When opening a file in python, it will just create the file if it does not exist
	# The 'r' tells python that we can read the file
	f.write('Test write this')
# can also write except IOError: (this will only work because that is the error we are producing)
except:
	print 'Error in writing to the file!' # This is why this does not error out when trying to open the file
else:
	print 'File write was a success'
finally: # Another example of finally. Again, this will always be run even if an error is hit
	print "Always execute finally code blocks"
	
print "\n"

# Example of using a try block with input from the user
# This will only work for one failed attempt

def askInt():
	try:
		val = int(raw_input("Please enter an integer: "))
	except:
		print "Looks like you did not enter an integer"
		val = int(raw_input("Try again. Please enter an integer: "))
	finally:
		print "Finally block executed"
	print val
		
askInt()