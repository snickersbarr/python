#!/usr/bin/python

### Exercise 30 ###
### Else and If ###

people = 30
cars = 40
trucks = 100


if cars > people:
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "We can't decice"

if trucks > cars:
	print "That's too many trucks."
elif trucks < cars:
	print "Maybe we could take the trucks."
else:
	print "We still can't decice"

if people > trucks:
	print "Alright, let's just take the trucks."
else:
	print "Fine, let's stay home then."