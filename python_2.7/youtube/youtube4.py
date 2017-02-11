#!/usr/bin/python

import math

yourAge = int(raw_input("How old are you: "))

#beginning of a an if statement ends in a colon
if (yourAge > 0) and (yourAge < 120):
	if (yourAge == 24):
		print "Same as me"
	elif (yourAge > 24):
		print "Older than me"
	elif (yourAge < 24):
		print "Younger than me"
else:
	print "Don't lie about your age"




