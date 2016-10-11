#!/usr/bin/python

# range function outputs a list
# range function (starting point and up to the stop point)
print range(0,10)

# range will default to start with 0, does the same as one above
print range(10)

x = range(0,10)
print x

# prints type of object, in this case x is a list
print type(x)

# range can use variables as well
start = 0
stop = 20
print range(start,stop)

# can specificy step interval with third argument
# in this case all even numbers
print range(start,stop,2)

# intervals of 3
print range(start,stop,3)

x = range(0,10)

for i in x:
	print i
	i += 1

l = [1,2,3,4,5]
print l

for num in l:
	print num

print '--------------------------'

# all range functions use up to
# if bigger numbers are used, will take up a lot of memory
for num in range(1,5):
	print num


# xrange allows you to generate numbers and uses less memory
for num in xrange(1,40):
	print num
	print '--------------------------'

# will just print the range and not the list
print xrange(1,40)

# xrange is it's own type
print type(xrange(1,40))

# prints as a list
z = range(1,40)
y = xrange(1,40)
print list(y)

# makes them the same
print z == list(y)
