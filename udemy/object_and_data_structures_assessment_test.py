#!/usr/bin/python
# from __future__ import division
# comment above will allow statements below to give correct output

a = 100.25
print 'a = ', a

b = 1**2*9/3+98.25-1
print b 

c = 2/3
print c

d = (2/3)
print d

e = 2.0/3.0
print e

print 4 * (6 + 5)
print 4 * 6 + 5
print 4 + 6 * 5

f = 3 + 1.5 + 4
print type(f)

s = 'hello'
print s[1]
print s[::-1]
print s[4]
print s[-1]

l = []
i = 0
while i < 3:
	l.append(0)
	print l
	i +=1

print '----Another Way----'
l =[0]
l = l * 3
print l

print '----Nested Lists----' ## Replacing 'hello' with 'goodbye'
l = [1,2,[3,4,'hello']]
l[2][2] = 'goodbye'
print l

print '----Sort Lists----'
l = [3,5,7,8]
print l
print sorted(l) # sorted function to sort list
l.sort() # another way to modify it
print l

print '----Dictionaries----'
d = {'simple_key':'hello'}
print d['simple_key']

print '----More Dictionaries----'
d = {'k1':{'k2':'hello'}}
print d['k1']['k2']

print '----More Dictionaries----'
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print d['k1'][0]['nest_key'][1][0]

print '----More Dictionaries (Holy fucking shit)----'
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print d['k1'][2]['k2'][1]['tough'][2][0]

print '----Lists and Sets----'
l = [1,2,2,33,4,4,11,22,3,3,2]
print set(l) # convert list to set with set() function

print '----Booleans----'
print 2 > 3 # false
print 3 <= 2 # false
print 3 == 2.0 # false
print 3.0 == 3 # true
print 4**0.5 != 2 # false
