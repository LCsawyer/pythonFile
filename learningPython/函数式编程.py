# -*- coding: UTF-8 -*-

#函数式编程抽象程度很高，函数没有变量所以输入确定输出确定，没有副作用

'''
#函数名可以被当成变量而赋给其它变量,所以一个函数就可以接收另一个函数作为参数
#称之为高阶函数

def f1(it) :
	print it
	
def f2(it,f):
	f(it+1)
f2(5,f1)
'''
#两个高阶函数map()和reduce（）
#map(,)传入两个参数一个函数一个序列，把函数作用于序列的结果返回一个list
'''
print map(str,[1,2,3,4])

def f1(x):
	return x*x       #f1函数应有返回值，否则无意义

print map(f1,[1,2,3,4]) 
'''
#reduce(,)接受的参数和map(,)一样，其作用如下所示：
#reduce(f,[a,b,c,d]) = f(f(f(a,b),c),d) 所以函数必须接受两个值，且列表至少有两个值
'''
def f1(a,b):
	return a*10 + b
print reduce(f1,[1,4,6,8,6,0])


def f1(str1):
	return str1.capitalize()

print map(f1,['adam','lisa','bart'])

def prod(list1):
	return reduce(lambda x,y: x*y,list1)
	
print prod([1,2,3,5,7,8,12])
'''

#filter()同样接受一个函数和一个序列，函数的作用是用来过滤序列，所以函数返回一个bool

def is_prime(at):
	ip1 = True
	if at != 1:
		for a1 in range(1,at/2 + 1):
			for a2 in range(1,at/2 + 1):
				if a1 * a2 == at:
					ip1 = False
	return ip1
print is_prime(6)
print filter(is_prime,range(1,101))

#高阶函数还有sorted()排序函数