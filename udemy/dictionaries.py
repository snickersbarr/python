#!/usr/bin/python

# creates a key with associated values
# associates keys with values separated with colons
# each set is separated with commas

my_dict = {'key1':'value','key2':'value2'}
print my_dict

# just like lists can have different data types (numbers and strings)

print my_dict['key1']

my_dict2 = {'k1':123,'k2':3.4,'k3':'string'}
print my_dict2['k3']

# calling parts of the indexed string
print my_dict2['k3'][0]

# cannot name a dictionary 'dict' : saved for something else 
my_dict3 = {'test':'test1'}
print my_dict3['test']
# can also call different methods on output
print my_dict3['test'].upper()

my_dict4 = {'k1':123,'k2':34,'k3':'string'}
print my_dict4

# does not change value of my_dict4 permanently
print my_dict4['k1'] - 120

# reassigning variable value will change permanently
my_dict4['k1'] = my_dict4['k1'] - 120
print my_dict4['k1']

my_dict4['k1'] = my_dict4['k1'] + 400
print my_dict4['k1']

# shorter notation using operator before equal sign for same result
my_dict4['k1'] += 100
print my_dict4['k1']

# creating an empty dictionary
d = {}
print d
# assigning keys and values to dictionary after creating empty dictionary

d['animal'] = 'Dog'
print d

# can also nest dictionaries the same way you can nest lists

# this example shows 'nestkey' nested within 'k1' and 'subnestkey' nested within 'nestkey' with a value of 'value'
d = {'k1': {'nestkey': {'subnestkey': 'value'}}}

# calling the different values within the nested dictionaries until we finally get just 'value'
print d
print d['k1']
print d['k1']['nestkey']
print d['k1']['nestkey']['subnestkey']

# again assigning keys and values to dictionaries after declaring empty dictionary
s = {}
s['k1'] = 1 
s['k2'] = 2
s['k3'] = 3
# note dictionaries are in no specific order due to referencing keys
print s

# print just the keys for the dictionary
print s.keys()
print s.values()
# print both keys and values in a tuple
print s.items()

