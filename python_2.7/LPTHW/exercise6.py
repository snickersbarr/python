#!/usr/bin/python

### Exercise 6 ###
### Strings and Text ###

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y # Nested formatting. Formatting done in the variable and again here

# Boolian assigned to variable hilarious.
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious # This is referencing the %r from the variable itself

# Example of string concatenation:
w = "This is the left side of..."
e = "a string with a right side."

print w + e
