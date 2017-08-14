# -*- coding: UTF-8 -*-
import time
import functools
import types
'''
#函数作为返回值，不会立即执行
def count():
	fs = []
	for i in range(1,4):
		
		def f():
			return i*i
		fs.append(f)
	return fs
#作为返回值得函数有传值参数时，被赋值的对象应该要传入相应参数例如
f1,f2,f3 = count() #该例中的f1()应为f1(i)
print f1(),f2(),f3()  #结果与期待的不同，因为函数并不会立即执行
'''

'''
#匿名函数lambda 支持有限，只能定义简单的函数
f = lambda x: x * x
print f(5)
'''
#任何函数都可以通过func(*args,**fw)的形式调用，无论它的参数是怎样的
#装饰器decorator,用于对函数进行补充但是又不对原函数重新定义
'''
def log(func):
	@functools.wraps(func)
	def wrapper(*ars,**kw):      #使用可变参数，以传入原函数传入的参数
		print "call %s():"%func.__name__
		func(*ars,**kw)   #执行被装饰函数的原功能
		
	return wrapper
@log
def now(iw):
	print iw ,time.ctime(time.time())
now(34)    #经过修饰后now(34)其实变成了log(now)(34)
print now.__name__
'''

#excise1
'''
def log(func):
	@functools.wraps(func)
	def wrapers(*arg,**ft):
		print 'begain call'
		func(*arg,**ft)
		print 'end call'
	return wrapers
@log
def now():
	print time.ctime(time.time())
now()
'''

#excise2

def log(text):
	def log2(func):
		@functools.wraps(func)
		def wrapers(*args,**fw):
			print '%s %s'%(text,func.__name__)
			func(*args,**fw)
		return wrapers
	if isinstance(text,types.FunctionType):
		return log2(text)
	else:
		return log2
@log
def func_1():
	print time.ctime(time.time())

@log('diff')
def func_2():
	print time.ctime(time.time())

func_1()
func_2()