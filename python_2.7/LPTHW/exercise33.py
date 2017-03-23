#!/usr/bin/python

### Exercise 33 ###
### While Loops ###

def test_function(i, runs, increment):
	numbers = []

	while i < runs:
		print "At the top i is %d" % i
		numbers.append(i)

		i += increment
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

	final_numbers = []

	for num in numbers:
		final_numbers.append(num)

	print "The final numbers: ", final_numbers

test_function(0, 9, 2)
test_function(3, 14, 4)