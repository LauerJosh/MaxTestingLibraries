#Welcome to Joshua 'Max' Lauer's own personal test library. Personally, I think Python's default Unittest is better, but enjoy all the same.

import sys, traceback, inspect

######UnitTesting
def testEqual(a, b): #Are these two values equal? Useful for testing for predicted output
	if(a != b):
		traceback.print_stack(inspect.currentframe().f_back, limit=1)
		print ("Test failed!\n{}\nis not equal to\n{}\n".format(a, b))

def testNotEqual(a, b): #Are these two values not equal? Useful for testing for predicted output
	if (a == b):
		traceback.print_stack(inspect.currentframe().f_back, limit=1)
		print ("Test failed!\n{}\nis equal to\n{}\n".format(a,b))

def testTrue(a): #Is this true? Mostly deprecated with testEqual and testNotEqual. Here for completion.
	if (a):
		pass
	else:
		traceback.print_stack(inspect.currentframe().f_back, limit=1)
		print ("Test failed! {} is false!".format(a))
		
def testFalse(a): #Is this false? Mostly deprecated with testEqual and testNotEqual. Here for completion.
	if(a):
		traceback.print_stack(inspect.currentframe().f_back, limit=1)
		print ("Test failed! {} is true!".format(a))

def testIs(a, b): #Are these the same? Useful for making sure the variables are truly identical
	if(a is b):
		pass
	else:
		traceback.print_stack(inspect.currentframe().f_back, limit=1)
		print("Test failed! {} is not the same as {}.".format(a,b))

def testIsNot(a, b): #Are these the same? Useful for making sure the variables are truly different
	if(a is b):
		traceback.print_stack(inspect.currentframe().f_back, limit=1)
		print("Test failed! {} is the same as {}.".format(a,b))
		
