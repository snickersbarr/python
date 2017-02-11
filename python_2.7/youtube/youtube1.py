#! /usr/bin/python

#Comments are made with hashes

import math
#from math import sqrt


integerEx = 8
longIntEx = 2000000000000000000000L
floatEx = 2.2
stringEx = "Hello"
booleanEx = True

print type(integerEx)
print type(longIntEx)
print type(floatEx)
print type(stringEx)
print type(booleanEx)

booleanTwo = False

print booleanEx and booleanTwo
print booleanEx or booleanTwo
print not booleanTwo

intOne = 7
intTwo = 99
floatOne = 7.9
floatTwo = 9.8
print intTwo / intOne
print float(intTwo) / float (intOne)
print int(floatOne)
print int(booleanEx)

print intOne > intTwo
print intOne < intTwo
print intOne >= intTwo
print intOne <= intTwo
print intOne != intTwo
booleanEx = intOne == intTwo


print intOne + intTwo
print intOne - intTwo
print intOne * intTwo
print intOne / intTwo
print intOne % intTwo
print intOne ** intTwo


print math.sqrt(intOne)

#answer = raw_input("What is your name? ")

#print "Hello " + answer
#print "Hello", answer



 #''' Allows you to type a multiline string
longStr = '''This is a long string of text 
that goes on and on'''


longStr2 = "This is also a string"
longStr3 = 'This also is a string'
longStr4 = '''This is a long string that will stay on this \
line because of the back slash'''
longStr5 = "He said 'Hi how are you doing'" '\n'

# '\n' for new line

another = "Hello"

print longStr
print longStr2
print longStr3
print longStr4
print longStr5
print another

