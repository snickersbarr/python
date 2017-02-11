#!/usr/bin/python

# Open the text.txt file in pwd
my_file = open('test.txt')

# We can now read the file
print my_file.read()

# Reset cursor to beginning of file to allow reading again
my_file.seek(0)
# Read each line. Does save it in memory. Not great for large text files
print my_file.readlines()

# For every line in object print line
for line in open('new.txt'):
	print line