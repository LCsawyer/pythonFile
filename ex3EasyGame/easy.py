# -*- coding: UTF-8 -*-

class easy(object) :
        
	def enter(self):
		print "you must be go thrugh there ,but there are a bear."
		print "you need get some way to through here."
		way = raw_input("chioce >")
		if way == 'fight' :
			return 'death'
		elif way == 'feed':
			return 'output'
		else :
			return 'death'
