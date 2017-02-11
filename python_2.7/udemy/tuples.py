#!/usr/bin/python

# construct a tuple
# in comparison to a list, uses () instead of []
# can also mix object types

t = (1,2,3)
t2 = (1,'test',3)
print t
print t2

# supports functions like len
# can call elements from index
print len(t)
print t2[1]

# calling index method to find location of elements
print t2.index('test')

# count method tells you how many times it appears in the tuple
print t2.count('test')
t3 = (1,1,1,3,4,1)
print t3.count(1)

# tuples are immutable and cannot be modified
l = [1,2,3]
t = (1,2,3)

print l
print t

l = 's'
# cannot reassign tuples the way you can with a list
