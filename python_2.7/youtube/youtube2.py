 #! /usr/bin/python


tupleEx = ('Kunal', 24, 'Santa Clara ', 'CA')

print tupleEx
print tupleEx [0]
print tupleEx [1]
print tupleEx [2]
print tupleEx [3]

tupleindividual = (66)

#tuple a tuple
tupleEx2 = tuple('abcd')
tupleEx3 = ('abcd')

print tupleEx2
print tupleEx3

#everything up to using :
print tupleEx2[0:3]

print tupleindividual


listNum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print listNum[-3:]
print listNum[:3]
print listNum[0:-3]

#shows even numbers
print listNum[1:10:2]

print len(listNum)
print min(listNum)

listMyName = list('Kunal')
print listMyName

#Appends with .join function
listMyName [5:] = ' Pamani'
print ''.join(listMyName)


listEx = ['Kunal', 24, 'Santa Clara ', 'CA']
print listEx


listEx2 = [1,2,3,4]
print listEx2

#uses this to replace
listEx2[1] = 5
print listEx2

#delete function to delete the 2nd variable from list
del listEx2[1]
print listEx2

print '\n'
#append to function to add to end of list
listEx.append('Holly')
print listEx

listEx.remove(listEx[3])
print listEx


listEx.insert(2, 'CA')
print listEx


