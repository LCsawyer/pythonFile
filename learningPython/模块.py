#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'a test module'   #文档注释使用__doc__访问，一定要放在会运行的代码的前面
from __future__ import division


__author__ = 'sawyer'

import sys
'''
def test():
	args = sys.argv
	if len(args) == 1:
		print "no arguments"
	elif len(args) == 2:
		print "hello!",_privatef(args[1])

if __name__ == '__main__':
	test()


#将函数或变量前加上_表示该函数或变量是该模块的私有变量

def _privatef(i):
	return i*i*i
'''

#__future__模块可以导入新版本中的一些用法，以方便过渡到新版
print __doc__

#导入新版的除法，/表示精确除法
print 4/3
