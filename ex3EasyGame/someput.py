# -*- coding: UTF-8 -*-

from sys import exit
class death(object):
	def enter(self):
		print "you are dead"
		exit(1)


class output(object):
	def enter(self):
		print "you win!"
		exit(0)

class in_put(object):
	def enter(self):
		print "please choice the pattern"
		print "please enter the easy , medium,hard and orthers"
		choice = raw_input('>')
		if choice == 'easy':
			return 'easy'
		elif choice == 'medium':
			return 'medium'
		elif choice == 'hard':
			return 'hard'
		else:
			return 'death'
