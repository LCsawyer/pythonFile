#!/usr/bin/env python
# -*- coding: UTF-8 -*-

u'描述了之前未接触的类的相关知识'

#私有变量，以__开头就是私有变量，但同时不要以__防止被视为类似于__name__的特殊变量
'''
class MyClass(object):
	def __init__(self,name,data):
		self.__name = name
		self.__data = data
	
	def print_data(self):
		print '%r : %r'%(self.__name,self.__data)

cc = MyClass('sawyer',45)

cc.print_data()
'''

#继承的多态体现在子类的函数可以覆盖从父类继承的函数

class Father1(object):
	def run(self):
		print "father is running" 

class Sun1(Father1):
	def run(self):
		print "son is running"

class Not_extend(object):
	def run(self):
		print u"哈哈，这样也行"

def try_run(father):
	father.run()
'''
try_run(Sun1())
try_run(Father1())
try_run(Not_extend())
'''
ase = Sun1()
#print dir(ase)     #dir()返回对象所有属性和方法的列表
#getattr(,),hasattr(,),setattr(,,)分别表示获得对象一个属性的、判断是否有该属性
#和设置一个属性（新增或改变都行）
setattr(ase,'sdata',67)  #setattr(,,)设置的属性只和对象绑定，中间的参数为属性名
print ase.sdata          #必须使用字符串表示，get和has也同样





















