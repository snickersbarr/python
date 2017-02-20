#!/usr/bin/python

### Exercise 8 ###
### Printing, Printing ###

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter) # This prints '%r' * 4 for each instance of formatter
print formatter % (
		"I had this thing.",
		"That you could type up right.",
		"But it didn't sing.", # This prints in double quotes because of the single quote in the string
		"So I said goodnight."
)