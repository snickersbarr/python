#!/usr/bin/python

# declare set with set()
x = set()
# add objects to set with .add method
x.add(1)

print x

x.add(2)
print x

# no change when adding same variable. Only cares about unique elements
x.add(1)
print x

l=[1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,]
print l

# will grab out unique elements from list
print set(l)

print '\n'
print '\n'


#### booleans ####
a = True
print a

# prints boolean answer to given equation
c = 11 > 2
print c

# none is a placeholder for an object that you don't want to reassign yet
b = None
print b

d = 2 > 11
print d

# reassigned b to string
b= 'a'
print b
