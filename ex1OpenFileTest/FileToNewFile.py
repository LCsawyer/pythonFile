# -*- coding: UTF-8 -*-

from sys import argv
from os.path import exists

script , filename , newFile = argv
'''
print "copy file from %r to %r." %(filename , newFile)

indata = open(filename).read()
print "the file data is %d bytes long" %len(indata)

print "is the file exist? %d" %exists(newFile)
print "hit ENTER to continue , and hit CTRL+C to abort"
raw_input('>')

otFile = open(newFile,'w')
otFile.write(indata)

print "ok, thats all!"

otFile.close()
'''
open(newFile,'w').write(open(filename).read())

