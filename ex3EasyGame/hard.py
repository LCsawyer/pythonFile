# -*- coding: UTF-8 -*-

class hard(object):
	def enter(self):
		print "you should guess 0 to 9"
		gdata = 6
		guess = raw_input('input>')
		
		if int(guess) != gdata :
			return 'death'
		else :
			print "go through---------------"
			print "monster here"
			goth = raw_input('chioce>')
			
			if goth == 'fight':
				return 'death'
			elif goth == 'hand':
				print "you should enter password to through"
				pass_word = '123'
				input_pass = raw_input('input>')
				if input_pass == pass_word :
					return 'output'
				else :
					return 'death'
			else :
				return 'death'
