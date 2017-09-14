# -*- coding:UTF-8 -*-
import time
from math import sqrt
'''
def adder(*args):
	print reduce((lambda a,b: a+b),list(args)) #性能较差，速度慢

def adder2(*args):
	sum = args[0];
	for i in args[1:]:
		sum += i
	print sum

list1 = [i for i in range(10000000)]

def testTime(func,*args):
	starttime = time.time()
	func(*args)
	elapstime = time.time() - starttime
	print func.__name__ , '-->' , elapstime

if __name__ == "__main__":
	testTime(adder,*list1)
	testTime(adder2,*list1)
'''
size = 1000
list1 = [x**2 for x in range(1000)]

def forgenf():
	res = []
	for x in list1:
		res.append(sqrt(x))
	return res


def mapf():
	return map(sqrt,list1)

def genf():
	return [sqrt(x) for x in list1]

def testTime(func,*args):
	starttime = time.time()
	for i in range(size):
		func(*args)
	elapstime = time.time() - starttime
	print func.__name__ , '-->' , elapstime


list2 = [forgenf,mapf,genf]

for x in list2:
	testTime(x)




































