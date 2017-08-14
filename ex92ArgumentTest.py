# -*- coding: UTF-8 -*-

from sys import argv

'''
script, first, second, third = argv

print "the scripe is called:", script
print "your first variable is:", first
print "your second vaiable is:", second
print "your third variable is:", third
'''

scripe , userName = argv
prompt = '>'

print "hi %s , i'm the %s scripe." %(userName , scripe)
print "i'd like to ask you a few question."
print "do you like me, %s?" % userName
likes = raw_input(prompt)

print "where do you live, %s?" % userName
lives = raw_input(prompt)

print "what kind of computer do you have?"
computer = raw_input(prompt)

print """
alright, so you said %r about liking me.
you live in %r. not sure where that is.
and you have a %r computer. nice.
""" % (likes , lives , computer)

print __name__
