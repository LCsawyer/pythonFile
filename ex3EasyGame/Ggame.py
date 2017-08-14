# -*- coding: UTF-8 -*-

from easy import easy  #作为模块的文件一般有.py,.pyc,.pyo,.pyd,.dll等
from hard import hard   #也可导入一个包（就是目录/文件夹），但文件夹中有__init__.py文件
from medium import medium #应用from '...' import '...'的格式可以导入模块中的某个对象
from someput import *


class Map(object):
	quips = {
		 'easy':easy(),
                 'in_put':in_put(),
		 'medium':medium(),
		 'hard':hard(),
		 'death':death(),
		 'output':output()}
	def __init__(self,first_map):
		self.first_map = first_map
	def next_scene(self,first_map):
		return Map.quips.get(first_map)
	def opening_scene(self):
		return self.next_scene(self.first_map)

class Engine(object):
	def __init__(self,start_map):
		self.start_map = start_map

	def play(self):
		print "欢迎来到不好玩的小游戏"
		current_scene = self.start_map.opening_scene()
		while True:
			print '-'*10
			next_scene = current_scene.enter()
			current_scene = self.start_map.next_scene(next_scene)


start_map = Map('in_put')

start_game = Engine(start_map)
start_game.play()
