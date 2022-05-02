"""
MonsterData

Holds all sprites for a given monster,
Assumes sprites follow the following format:

Stand:		*_0.png	 | *_1.png 
Walk: 		*_2.png	 | *_3.png 
Run: 		*_4.png	 | *_5.png 
Exercise: 	*_6.png  | *_7.png 
Happy: 		*_8.png
Sleep: 		*_9.png
"""

import pygame
from os import listdir
from os.path import exists
from random import randint

class MonsterData():
	def __init__(self,spritedir):

		self.name = spritedir

		self.evo_list = []

		evo_file = open('monsters/' + spritedir + '/evos.txt',"r")
		for m in evo_file:
			self.evo_list.append(m.split('\n')[0])

		sprites = listdir('monsters/' + spritedir)
		for spr in sprites:
			if '_0.png' in spr:
				prefix = spr.split('_')[0]


		if len(sprites) >= 10:
			self.spritedict = {
				'stand' : [
					pygame.image.load('monsters/' + spritedir + '/' + prefix + '_0.png'),
					pygame.image.load('monsters/' + spritedir + '/' + prefix + '_1.png')
				],
				'walk' : [
					pygame.image.load('monsters/' + spritedir + '/' + prefix + '_2.png'),
					pygame.image.load('monsters/' + spritedir + '/' + prefix + '_3.png')
				],
				'run' : [
					pygame.image.load('monsters/' + spritedir + '/' + prefix + '_4.png'),
					pygame.image.load('monsters/' + spritedir + '/' + prefix + '_5.png')
				],
				'exercise' : [
					pygame.image.load('monsters/' + spritedir + '/' + prefix + '_6.png'),
					pygame.image.load('monsters/' + spritedir + '/' + prefix + '_7.png')
				],
				'happy' : [
					pygame.image.load('monsters/' + spritedir + '/' + prefix + '_1.png'),
					pygame.image.load('monsters/' + spritedir + '/' + prefix + '_8.png')
				],
				'sleep' : [
					pygame.image.load('monsters/' + spritedir + '/' + prefix + '_9.png'),
					pygame.image.load('monsters/' + spritedir + '/' + prefix + '_9.png') \
					if not exists('monsters/' + spritedir + '/' + prefix + '_12.png') \
					else \
					pygame.image.load('monsters/' + spritedir + '/' + prefix + '_12.png')
				]
			}

		elif len(sprites) <= 9:
			self.spritedict = {
				'stand' : [
					pygame.image.load('monsters/' + spritedir + '/' + prefix + '_0.png'),
					pygame.image.load('monsters/' + spritedir + '/' + prefix + '_1.png')
				],
				'walk' : [
					pygame.image.load('monsters/' + spritedir + '/' + prefix + '_1.png'),
					pygame.image.load('monsters/' + spritedir + '/' + prefix + '_2.png')
				],
				'run' : [
					pygame.image.load('monsters/' + spritedir + '/' + prefix + '_1.png'),
					pygame.image.load('monsters/' + spritedir + '/' + prefix + '_2.png')
				],
				'exercise' : [
					pygame.image.load('monsters/' + spritedir + '/' + prefix + '_0.png'),
					pygame.image.load('monsters/' + spritedir + '/' + prefix + '_1.png')
				],
				'happy' : [
					pygame.image.load('monsters/' + spritedir + '/' + prefix + '_1.png'),
					pygame.image.load('monsters/' + spritedir + '/' + prefix + '_8.png')
				],
				'sleep' : [
					pygame.image.load('monsters/' + spritedir + '/' + prefix + '_9.png'),
					pygame.image.load('monsters/' + spritedir + '/' + prefix + '_9.png')
				]
			}

	def get_next_monster(self):
		sel = randint(0,len(self.evo_list)-1)
		return self.evo_list[sel]
