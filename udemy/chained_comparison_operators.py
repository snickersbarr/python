#!/usr/bin/python

print 1 < 2
print 2 < 3

# Can chain together comparison operators
print 1 < 2 < 3

# same can be written with and statement
# both statements must be true with 'and' for boolean output to be true
print 1 < 2 and 2 < 3

# only one statement needs to be true for 'and' statement for boolean output to be true
print 1 < 2 or 3 < 2

# both are false, therefore output is false
print 1 > 3 or 3 < 2

