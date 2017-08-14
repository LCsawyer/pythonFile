# -*- coding: UTF-8 -*-
from sys import exit
#a parent class Scene
class Scene(object):
	def enter(self):
		print "this is empty"
		exit(1)

# the class Engine use to run game
class Engine(object):
	def __init__(self,scene_map):   #input a Map object to 
		self.scene_map = scene_map #initialize it

	def play(self):
		curent_scene = self.scene_map.opening_scene()#return a Map object
		while True:
			print '-'*10
			next_s = curent_scene.enter()    #return a string
			curent_scene = self.scene_map.next_scene(next_s) #return a Map object


class central_corridor(Scene):
	def enter(self):
		print "en,i don't know. ok,我试试汉语"
		print "好像有点用"
		print "please choice a , b , c or others"
		action = raw_input('>')
		if action == 'a':
			print "this is mistake"
			return 'death'
		elif action == 'b':
			print "en en,NO!"
			return 'death'
		elif action == 'c':
			print "ok , you are lucky!"
			return 'laser_weapon_armory'
		else :
			print "dose not compute"
			return 'central_corridor'

class laser_weapon_armory(Scene):
	def enter(self):
		print "there is a keypad lock on the box."
		print "if you get the code wrong 10 times then the lock"
		print "close forever and you can't get the bomp."
		print "the code is 3 digits."
		code = "666" 
		guess = raw_input('[Keypad]>')
		guesses = 0
		while guess != code and guesses < 10:
			print "BZZEDDD"
			guesses += 1
			guess = raw_input('[Keypad]>')
		if guess == code:
			print "you can go next"
			return 'the_bridge'
		else :
			return 'death'

class the_bridge(Scene):
	def enter(self):
		print "please choice a , b or others"
		action = raw_input('>')
		if action == 'a':
			print 'WRONG'
			return 'death'
		elif action == 'b':
			print '	lucky'
			return 'escape_pod'
		else:
			print "dose not compuse"
			return 'the_bridge'


class escape_pod(Scene):
	def enter(self):
		print "please enter 1 to 5"
		print "you just have one time"
		good_pod = 1
		guess = raw_input('Keypod>')
		if int(guess) == good_pod:
			print "you win"
			exit(0) 
		else:
			print "	WRONG"
			return 'death'


class death(Scene):
	def enter(self):
		print "Such a luser"
		exit(1)
class Map():
	scene = {'central_corridor' : central_corridor(),
		 'laser_weapon_armory' : laser_weapon_armory(),
		 'the_bridge' : the_bridge(),
		 'escape_pod' : escape_pod(),
		 'death' : death()}
	def __init__(self,start_scene):
		self.start_scene = start_scene
	def next_scene(self,scene_name):
		return Map.scene.get(scene_name)	
	def opening_scene(self):
		return self.next_scene(self.start_scene)






start_map = Map('central_corridor')
start_game = Engine(start_map)
start_game.play()
















	
