#!/usr/bin/python

### Exercise 10 ###
### What Was That? ###

# escape sequence
print "I am 5'11\" tall." # escape double-quote inside string
print 'I am 5\'11" tall.' # escape single-quote inside string

tabby_cat = "\tI'm tabed in." # \t tabs in
persian_cat = "I'm split\non a line." # \n for a new line
backlash_cat = "I'm \\ a \\ cat." # \\ to show one '\'

# example of multiline tabs
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backlash_cat
print fat_cat

'''
Interesting piece of code that will never stop:

while True :
	for i in ["/" ,"-" ,"|" ,"\\" ,"|"]:
		print "%s\r" % i ,
'''