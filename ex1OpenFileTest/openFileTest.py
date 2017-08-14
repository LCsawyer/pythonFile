# -*- coding: UTF-8 -*-

from sys import argv

script , filename = argv

'''
txt = open(filename)

print "here.s your file %r:" % filename
print txt.read()

print "type the filename again:"
fileAgain = raw_input('>')

txtAgain = open(fileAgain)
print txtAgain.read()
print "Œ“ø¥ø¥"
'''

print "we're going to erase %r." % filename
print "if you don't want that , hit CTRL-C(^C)."
print "if you do want that, hit ENTER."

raw_input("?")

print "opening the file..."
target = open(filename, 'w')

print "truncating the file. goodbye!"
#target.truncate()

print "now i'm going to ask you for three lines."

line1 = raw_input('line1: ') + '\n'
line2 = raw_input('line2: ') + '\n'
line3 = raw_input('line3: ') + '\n'

print "writing..."
'''
target.write(line1); target.write('\n')
target.write(line2); target.write('\n')
target.write(line3)
'''
target.write(line1+line2+line3)
print "ok, closing..."
target.close()

