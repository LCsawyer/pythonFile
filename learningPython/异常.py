#!usr/bin/env python
# -*- coding: UTF-8 -*-
#u'异常的相关知识介绍'
import logging
#异常使用try捕捉异常,使用except判断是何种异常,finally是一定会运行的部分
#使用logging模块可以记录并打印出错的详细信息(包括出错的位置)
'''
def f1(i):
	print 8/i
try :
	print u'出错前'
	
	f1(0)
	print u'没出错'
except StandardError,e:
	#print e
	logging.exception(e)
	raise
finally :
	print u'我肯定是要执行的'
print 'END'
'''
#raise用来显示地引发异常，既抛出异常，后面的程序就不会在运行，
#就想平时程序出错一样，若不带参数相当于将异常原样抛出
'''
try:
	10 / 0
except ZeroDivisionError:
	raise ValueError('input error!')
print 'END'
i = 9
hj = i*8
raise ValueError('input error')
print hj
'''

#使用assert(断言)可以用来确定出错的原因及位置
n1 = input('enter a interger>')
#assert n1 != 0 ,'n is zero!'
print 10/n1    #比之前的仅仅知道出错的类型更加精确
#在启动python解释器时使用 -o参数关闭断言(python -o 异常.py)


