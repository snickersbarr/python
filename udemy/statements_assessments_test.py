#!/usr/bin/python

st = "Print only the words that start with s in this sentence"
for word in st.split(): # For every element(word) in st with split() method. Split method separates individual strings as elements
	if word[0] == 's': # if the first index of the element in the string is 's'
		print word # print that word

# Print all even numbers from 0 to 10
print "---- Next subtest ----"
for num in range(11):
	if num%2 == 0:
		print num

print "---- Another Way ----"
print range(0,11,2)

# Use list comprehension to create a list of all numbers between 1 and 50 divisible by 3
print "---- Next subtest ----"
lst = [number for number in range(1,51) if number % 3 == 0]
print lst

st = "Print every word in this sentence that has an even number of letters"
for word in st.split():
	if len(word) % 2 == 0:
		print word, '<---- has an even length'
		
lst = range(1,101)
for num in lst:
	if num % 3 == 0:
		print 'Fizz'
	if num % 5 == 0:
		print 'Buzz'
	if num % 3 == 0 and num % 5 == 0:
		print 'FizzBuzz'
	else:
		print num
		
st = 'Create a list of the first letters of every word in this string'
lst = [word[0] for word in st.split()]
print lst