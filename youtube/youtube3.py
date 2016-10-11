#!/usr/bin/python

import math

#creating a dictionary
dictEx = ({"Age":35, "Height":"5'11","Weight":178})
print dictEx

#get is a function
print dictEx.get("Height")

#print out keys and values using items
print dictEx.items()

#print values and not keys
print dictEx.values()

#deleting a value from a dictionary
dictEx.pop("Height")
print dictEx

strName = 'Holly'
floatAge = 27.4
charSex = 'F'
intKids = 0
boolMarried = False

#They do the same thing, no extra space required with a comma
print 'My name is ', strName
print 'My name is ' + strName



#uses %s for string and %f for float as replacements for variables declared later
print '%s is  %f years old' % (strName, floatAge)
#us a point followed by number to declare how many decimal spaces
print '%s is  %.1f years old' % (strName, floatAge)

# %c for character
print 'Sex: %c' % (charSex)

# %d for integer
print 'She has %d kids and said it\'s %s she is not married.' % (intKids, boolMarried)

#print pi to the 15th decimal place
print 'pi to the 15th decimal place is %.15f' % (math.pi)

#spacing
print '%20f' % (math.pi)
print '%20.15f' % (math.pi)

#right justified with negative sign
print '%-25.15f is pi' % (math.pi)

#int is converting string from raw_input to int from user
####  precisionPi = int(raw_input("How precise should pi be: "))

#using .*to determine what precision wil lbe based on input
####  print 'Pi = %.*f' % (precisionPi, math.pi)


bigString = 'Here is a long string that I will be messing with' + ' | and some more.'

print bigString

#picking out letters
print bigString[1:20:2]

#find function
print bigString.find('string')

#count how many occurences of letter e
print bigString.count('e')
print bigString.count('e', 4, 20)

#turns into tuple
copyStr = tuple(bigString)

print copyStr

#turns back into string
print ', '.join(copyStr)

print bigString.upper()
print bigString.lower()

#replaces long with small
print bigString.replace('long', 'small')

#strips spaces and splits words
print bigString.split(' ')

#strip function gets rid of white space
randomWhite = '       Random white space         '
print randomWhite.strip()