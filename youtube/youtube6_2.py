#!/usr/bin/python

globalTen = 10

#accept unlimited amount of arguments
def addNumbers(*args):
	finalValue = 0 #local variable, only available within function
	
	globalTen = 15 #does nothing, cannot change global variable within function
	if args:
		for i in args:
			finalValue += i
		return finalValue
	else:
		return "Please provide numbers"

def main():
	print addNumbers(30,30,13,30,50)
	print globalTen

if __name__ == '__main__': main()