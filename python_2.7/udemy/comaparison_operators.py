#!/usr/bin/python

"""
Operator	Description	Example
==	If the values of two operands are equal, then the condition becomes true.	
	(a == b) is not true.
!=	If values of two operands are not equal, then condition becomes true.	
	(a != b) is true
<>	If values of two operands are not equal, then condition becomes true.	
	(a <> b) is true. This is similar to != operator.
>	If the value of left operand is greater than the value of right operand, then condition becomes true.	
	(a > b) is not true.
<	If the value of left operand is less than the value of right operand, then condition becomes true.	
	(a < b) is true.
>=	If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.	
	(a >= b) is not true.
<=	If the value of left operand is less than or equal to the value of right operand, then condition becomes true.	
	(a <= b) is true.
"""


# Prints boolean outputs for comparison operators:
a = 2 == 2
print a

b = 1 == 0
print b

c = 3 <> 4
print c

d = 5 > 4
print d

e = 5 < 4
print e

f = 5 >= 4
print f

g = 5 <= 4
print g

# don't need a variable to get output
print 2 < 3

