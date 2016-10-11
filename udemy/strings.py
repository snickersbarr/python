#!/usr/bin/python

print('Hello World') #for Python 3, although seems like it works in both
# from __future__ import print

print 'Hello'
print 'This is also a string'
print "This is a string"
print '"How to use quotes"'

print 'Here is a new line \nand here is the second line \nand the third.'
print 'Here is a \ttab'

print len('Hello World') #counts characters (includes spaces)

s = 'Hello World again'
print s
print s[0]
print s[1:] #Everything for designated point onwards
print s[:3] #Everything up to 3, not including 3
print s[-1] #Last letter
print s[:-1] #Everything but last letter
print s[::2] #Every other
print s[::-1] #reverse string

print 'immutability' #cannot change particular elements in sequence

s = s + ' concatenate me!'
print s

letter = 'zz'
print letter

letter = letter*10
print letter

s = 'Hello'
print s

s = s.upper()
print s

s = s.lower()
print s

s = s.split('e') #splits where that element occured
print s