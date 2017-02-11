#!/usr/bin/python

globalTen = 10

#accept unlimited amount of arguments
def changeGlobal():
	global globalTen
	globalTen = 15

def main():
	print globalTen
	changeGlobal() #calling the change global function
	print globalTen
	
if __name__ == '__main__': main()