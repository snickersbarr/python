#!/usr/bin/python

st = 'Print only the words that start with s in this sentence'
print st
for word in st.split():
	if word[0] == 's':
		print word

print '------------'
print ('all even numbers from 0-10')
print range(0,11,2)

print '------------'
print ('Use List comprehension to create a list of all numbers between 1 and 50 that are divsible by 3.')
l = []
for number in range(1,51):
	if number %3 == 0:
		l.append(number)
print l
[x for x in range(1,50) if x %3 == 0]

print '------------'
st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
	if len(word)%2 == 0:
		print word+" <-- has an even length"

l = range(1,101)
for num in l:
	if num %3 == 0:
		print "Fizz"
	if num %5 == 0:
		print "Buzz"
	if num %3 == 0 and num %5 == 0:
		print "FizzBuzz"
	else:
		print num

st = 'Create a list of the first letters of every word in this string'
print st
l = []
for word in st.split():
	l.append(word[0])
print l
	