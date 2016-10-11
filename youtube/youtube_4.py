#!/usr/bin/python

globalTen = 10

#accept unlimited amount of arguments
def createDict(**kpargs):
	for i in kpargs:
		print i, kpargs[i] #prints a new line with every argument passed through
	print type(kpargs)
	return
	
def main():
	createDict(cust1=('Derek',35,1974),cust2=('Kunal',24,1992)) #Can input multiple tuples into the function

	
if __name__ == '__main__': main()