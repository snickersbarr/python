#!/usr/bin/python

# break (Breaks out of the current closing enclosing loop)
# continue (Goes to the top of the closest enclosing loop)
# pass (Does nothing at all)

x = 0
while x < 10:
	print 'x is currently: ',x
	print ' x is still less than 10, adding 1 to x'
	x += 1
	
	if x==3:
		print ' Hey, x equals 3!'
#		break, if this existed here, it will stop the out while loop at 3
	else:
		print 'continuing...'
		continue
# be careful with while loops, should always have a break to stop the loop at some point
''' 
while True:
	print 'Uh oh infinite Loop!'
'''
