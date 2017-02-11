#!/usr/bin/python

#Prints odd numbers in desired range
listEx = range(1,60)

for i in listEx:
	if (i%2) == 0:
		continue
	else:
		print i,


print '\n'

listEx2 = range(1,20)

for z in listEx2:
	if (z%2) == 0:
		continue
	elif z == 11:  #tells the for loops to stop at 11 with break 
		break
	else:
		print z,