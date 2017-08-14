# -*- coding: UTF-8 -*-
'''
list1 = [1,2,3,4,5]
list2 = ['sawyer','bob','james','jake']
list3 = ['cpp',1,'python','2','java',3]

for i in list1 :
	print "this is %d "% i,

print "\n"

for i in list2 :
	print i,

print "\n"
for i in list3 :
	print i,
	
print '\n'

ls = []

for i in range(0,6) :   #从0开始到6（不包括6）默认步长为1，可以有第三个参数表示步长
	data = raw_input('>')
	ls.append(data)

print ls;
'''

from sys import exit

def gold_room() :
	print "this room is full of gold ,how much do you take"
	next = raw_input(">")
	if next.isdigit():
	    how_much = int(next)
	else :
		dead("man, learn to tyoe a number.")
	
	if how_much < 50 :
	    print "Nice , you're not greedy, you win!"
	    exit(0)
	else :
	    dead("you greedy bastard!")


def bear_room() :
	print "three is a bear here."
	print "the bear has a bunch of honey."
	print "the fat bear is in front of another door."
	print "how are you going to move the bear?"
	bear_moved = False
	
	while True :
		next = raw_input(">")
		
		if next == "take honey" :
		    dead("the bear looks at you then slaps your face off.")
		elif next == "taunt bear" and not bear_moved :
		    print "The bear has moved from the door. You can go through it now."
		    bear_moved = True
		elif next == "open door" and bear_moved :
		    gold_room() 
		else:
		    print "i got no"

def cthulhu_room():
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"
	
	next = raw_input('>')
	
	if "flee" in next :
	    start()
	elif "head" in next :
	    dead("well that was tasty!")
	else:
	    cthulhu_room()

def dead(why) :
	print why, "good job!"
	exit(0)
	
def start() :
	print "you are in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take?"
	print "please choice 'left' or 'right',don't chioce others"
	next = raw_input('>')
	
	if next == "left":
	    bear_room()
	elif next == "right":
	    cthulhu_room()
	else :
	    dead("You stumble around the room until you starve!")

start()		