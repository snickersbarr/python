#!/usr/bin/python

print 'This is a string'

x = 13.13
print 'Place my variable here: %s' %(x)

#fist number is total minimum number of digits this string should contain
#number after is how many digits after decimal point

print 'Floating point number: %1.1f' %(13.145)
print 'Floating point number: %1.2f' %(13.145)
print 'Floating point number: %1.3f' %(13.145)
print 'Floating point number: %25.3f' %(13.145)
print 'Convert to string %s' %(123)
print 'First: %s, Second: %s, Third: %s' %('hi','two',3)
print 'First: %s, Second: %s, Third: %s' %(x,x,x)
print 'First: %s, Second: %s, Third: %s' %(2,2,2)

#.format allows you to use {} and order does not matter, can assign values to variables
print 'First: {x}, Second: {x}, Third: {y}'.format(x='inserted',y='two!')
print 'My name is {x} and my last name is {y}'.format(x='Kunal',y='Pamani!')

#Python 3
print ('hello')

print ('One: {x}'.format(x='INSERT ME!'))
