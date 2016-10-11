#!/usr/bin/python

# constructed with square brackets and commas to separate elements
my_list = [1,2,3]
print my_list
# lists can hold different object types (strings, integers, floats)

my_list=['string',23,1.2,'o']
print my_list

print len(my_list)

my_list = ['one','two','three',4,5]
print my_list

my_list[0]
'one'

# call individual elements or sets of elements
z = my_list[:1]
y = my_list[0]
x = my_list[1:]
w = my_list[:3]

print z
print y
print x
print w

# concatenate
a = my_list + my_list
print a

# when concatenating with string reques ['']
my_list = my_list + ['wooo']
print my_list

# multiplies lists
b = my_list * 5
print b

l = [1,2,3]
print l

# method so redeclares variable while appending
l.append('asa')
print l

l.append('and other one')
print l

# pop method removes one element. In this example removing first element with the position of 0
l.pop(0)
print l

# even while using pop method and assigning to variable, it changes value of l
x = l.pop(0)
print x
print l

# l.pop(99) this would give an error because it is outside of the paremeters of the list

new_list = ['a','e','x','b','c',]
print new_list

# reverses method simply reverses list
new_list.reverse()
print new_list

# sort method sorts alphabetically by default
new_list.sort()
print new_list

l_1 = [1,2,3]
l_2 = [4,5,6]
l_3 = [7,8,9]

# nesting data structures. for this example list inside of a list
matrix = [l_1,l_2,l_3]
print matrix

# this returns nested list as first element
print matrix[0]

# can grab element within element
print matrix[0][0]

print matrix[1][1]
print matrix[2][0]

# prints first column of the matrix created. This is called list comprehension
first_col = [row[0] for row in matrix]
print first_col

test_list = [1,2,3]
print test_list.pop()

test_list2 = [1,2,3]
print test_list2[1:]

