#!/usr/bin/python

### Exercise 16 ###
### Reading and Writing Files ###

"""
This exercise opens a file.
It will create the file if it does not exist.
It will then clear the contents of the file with .truncate()
Then allows the user to input each line to the file.
This uses argv, to let the user designate the name of the file.
"""
from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, it CTRL-C (^C)."
print "If you do want that, hit return"

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()
print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1, line2, line3)

print "And finally, we close it."
target.close()