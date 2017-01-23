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
	
try:
	f = open('testfile1231', 'w') # When opening a file in python, it will just create the file if it does not exist
	# The 'w' tells python that we can write to the file
	f.write('Test write this')
except:
	print 'Error in writing to the file!' # This is why this does not error out when trying to open the file
else:
	print 'File write was a success'
	
