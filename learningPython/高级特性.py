#-*- coding: UTF-8 -*-
from collections import Iterable #Iterable表示可迭代对象
#python中的迭代:
'''
d = {'a':1,'b':2,'c':3}
for key in d.keys():         #抽象层次高可用于很多对象，list、tuple、dic、string等
	print d[key]         #dic默认迭代key值可以用iteritems()迭代value



print isinstance([1,2,3],Iterable) #isinstance(,)用来判断一个对象是否输入后面的类别
print isinstance(1,(int,str)) #第二个参数可以是包括多个类的元组，前一个只要包括其中就返回True
'''

#列表生成式，可以使用range(,)生成包含一定范围内连续的整数的list
'''
print range(1,10)
L = []
for i in range(1,10):
	if i%2 == 0 :
		L.append(i*i)

# or

L2 = [i*i for i in range(1,10) if i % 2 == 0]
#对于一些简单的迭代也可以写成上面那样
print L
print L2
'''

#生成器Generator,功能很强大，可以将列表函数等转换成生成器
#将列表的[]改成()就可以了
list1 = (x*x for x in range(10))
print list1.next()        #next()是与list的最大区别，一般用于创建几个元素而避免创建整个list

#其主要用处还是在于函数

def fib(max):
	n,a,b = 0,0,1
	while n<max:
		yield b          #yield作为返回的地方，再执行next()时从此处开始继续运行直到下个yiekd
		a,b = b , a+b
		n += 1

print fib(6).next(),fib(6).next()

for i in fib(8):        #同样它可迭代
	print i, 

print isinstance(fib(8),Iterable)  #生成器输入可迭代对象