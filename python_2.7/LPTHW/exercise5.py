#!/usr/bin/python

### Exercise 5 ###
### More Variables and Printing ###

my_name = 'Kunal Pamani'
my_age = 25
my_height = 71 # inches
my_weight = 175 # lbs
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Brown'

# %d is used for integer decimals
# %s is used for strings. Will convert to a string if it is not a string

print "Let's taalk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# Tricky line for formatting. Variables go in order they are referenced
print "If I add %d, %d, and %d, I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

# Extra
# Rounding numbers example:

first_variable = 1.777
print first_variable

print round(first_variable)