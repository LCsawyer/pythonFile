# -*- coding: UTF-8 -*-
'''
class Song(object) :
	def __init__(self , lyrics) :
		self.lyrics = lyrics
	
	def sing_me_a_song(self) :
		for line in self.lyrics :
			print line ,


song1 = 'asdfgh'
song3 = "abcdefghijklmnopqrstuvwxyz"

happy_bday = Song(["happy birthday to you" , 
                  "i don't want to get sued" ,
                  "so i'll stop right there"])

bull_on_parade = Song(["They rally around the family",
                       "With pockets full of shells"])


happy_bday = Song(song1)
bull_on_parade = Song(song3)
happy_bday.sing_me_a_song()
bull_on_parade.sing_me_a_song()
'''

from sys import exit
from random import randint
class Game(object) :
	def __init__(self , start) :
		self.start = start
	def play(self):
		next = self.start
		while True:
			print "\n-------"
			room = getattr(self,next)
			next = room()
	def death(self) :
		quips = ["You died.  You kinda suck at this.",
				"Nice job, you died ...jackass.",
				"Such a luser.",
				"I have a small puppy that's better at this."]
		print quips[randint(0,len(quips)-1)]
		exit(1)

	def central_corridor(self) :
		print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
		print "please choice %r , %r , %r or others" %('shoot','dodge','tell a joke')
	
		action = raw_input('>')
	
		if action == "shoot" :
			print "you are very brave. but he is so strang."
			print "so you can't beat he . and he eats you."
			print "you are dead!"
			return 'death'
		elif action == "dodge" :
			print "you can't dodge. you are dead!"
			return 'death'
		elif action == "tell a joke" :
			print "you're very lucky . you can go though"
			return 'laser_weapon_armory'
		else :
			print "does not compute!"
			return 'central_corridor'

	def laser_weapon_armory(self) :
		print "you must be input a code to gothrough"
		print "the code is 3 digits"
		code = "666"
	
		guess = raw_input("[Keypad]>")
		guesses = 0
	
		while guess != code and guesses < 10 :
			print "BZZZZZEDD"
			guesses += 1
			guess = raw_input("[Keypad]>")
	
		if guess == code :
			print "The container clicks open and the seal breaks, letting gas out."
			return 'the_bridge'
		else :
			print "You decide to sit there"
			return 'death'

	def the_bridge(self) :
		print "you must be take control of the ship."
		print "take chioce",
		print "a 、'throw the bomb' ,b 、'slowly place the bomp '"
	
		action = raw_input('>')
	
		if action == 'a' :
			print " You die knowing they will probably blow up when it goes off."
			return 'death'
		elif action == 'b' :
			print "Now that the bomb is placed you run to the escape pod to"
			return 'escape_pod'
		else :
			print "does not compute!"
			return 'the_bridge'

	def escape_pod(self) :
		print "you should chioce one of 5"
	
		good_pod = randint(1,5)
		guess = raw_input("[pod#]>")
	
		if int(guess) != good_pod :
			print "sorry, that's wrorry!"
			return 'death'
		else :
			print "you won!"
			exit(0)


game_run = Game('central_corridor')
game_run.play()