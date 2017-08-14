# -*- coding: UTF-8 -*-

from sys import argv

script , infile = argv

def p_all(f):
	print f.read()

def rewind(f):
	f.seek(0)

def p_aline(lcount,f):
	print lcount , f.readline(),

cfile = open(infile)
p_all(cfile)
rewind(cfile)
cl = 1;
p_aline(cl,cfile)
p_aline(cl + 4,cfile)
p_aline(5,cfile)

