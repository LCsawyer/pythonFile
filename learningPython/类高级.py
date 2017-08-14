#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from types import MethodType
import time
#可以对类、对类的实例进行相关属性的动态绑定，以添加新的属性
'''
class Student(object):
	pass

st = Student()
st.name = 'Sawyer'  #只对st对象添加name属性，Student类中任不包含该属性，其它实例自然也不包含

def set_name(self,name):
	self.name = name    #为实例添加并绑定函数，需要使用MethodType()
st.set_name = MethodType(set_name,st,Student)
                         #MethodType()的第二个参数为None时表示为类绑定函数
st.set_name('ert')
print st.name
'''
#使用__slots__=()限制属性的绑定，()中包括允许绑定的属性
'''
class Student(object):
	__slots__=('name','data')
st = Student()
st.name = 'sawyer'
#st.age = 34   #wrong
def set_name(self,name):
	self.name = name  
st.set_name = MethodType(set_name,st,Student) #wrong 同样适用于函数
st.set_name('as')
print st.name
#Student.name = 'sawyer'   #这样做使类绑定了一个属性导致对象对该属性只读
#st.name = 'cc'  #wrong
#print st.name
'''

#使用@property将类中的某些方法转变成属性，以控制外部对属性的访问
'''
class Student(object):
	@property         #getter
	def score(self):
		return self.__score
	@score.setter      #setter
	def score(self,value):
		if not isinstance(value,int):
			raise ValueError('score must be int')
		if value < 0 or value > 100:
			raise ValueError('score must between 0~100')
		self.__score = value
	@property    #仅仅设置getter
	def timep(self):
		return time.ctime(time.time())

st1 = Student()
st1.score = 20

print st1.score,st1.timep
'''

#类中的一些特殊用途的函数__...__这种形式的
#__str__()函数用来显示类的实例的相关信息，可以不用默认的自己定义
#__repr__()和__str__()作用相似，一个为用户服务一个为调试服务
#__iter__()返回一个可迭代的对象(还是该实例对象，只不过它可迭代)
#定义一个next()函数就可以返回下一个值
'''
class Fib(object):
	def __init__(self):
		self.a,self.b = 0,1
	def __iter__(self):
		return self
	def next(self):
		self.a,self.b = self.b,self.a + self.b
		if self.a > 1000000:
			raise StopIteration()
		return self.a
for n in Fib():
	print n
'''

#使用__getitem__()使类像list、tuple一样可以进行[i]取值操作
'''
class Fib(object):
	def __getitem__(self,n):
		a,b = 1,1
		for x in range(n):
			a,b = b,a + b
		return a
print Fib()[40]
'''

#此外还有__getattr__()用来调用没有找到的属性
#__call__()使对象能够以f()的形式运行以达到特定的功能
'''
class Chain(object):
	def __init__(self,path=''):
		self.path = path
	def __getattr__(self,path):
		return Chain("%s/%s"%(self.path,path))
	def __str__(self):
		return self.path
	def __len__(self):
		return len(self.path)

print Chain().status.user.timline.list
'''
















