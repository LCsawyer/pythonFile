# -*- coding: UTF-8 -*-
'''
def print_two(*args):
    arg1 , arg2 = args
	print "arg1: %r, arg2: %r" %(arg1 , arg2)
'''
def print_again(a1 , a2):
	print "a1: %r , a2: %r" %(a1 , a2)

def print_none():
	print "is ok."
def print_two(*args):  #它的功能是告诉 python 
	a1 , a2 = args     #让它把函数的所有参数都接受进来，然后放到名字叫 args 的列表中去。
	print "arg1: %r, arg2: %r" %(a1 , a2)
print_two("asd","sa")
print_again("adf","wqert")
print_none()

