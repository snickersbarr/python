#!/usr/bin/python

### Exercise 11 ###
### Asking Questions? ###

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

# Weird how this does not work in Sublime Text.app but does work in Terminal