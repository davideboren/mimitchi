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

class MonsterData():
	def __init__(self,spritedir):

		sprites = listdir('monsters/' + spritedir)
		prefix = sprites[0].split('_')[0]

		self.spritedict = {
			'stand' : [
				pygame.image.load('monsters/' + spritedir + '/' + prefix + '_0.png'),
				pygame.image.load('monsters/' + spritedir + '/' + prefix + '_1.png')
			],
			'walk' : [
				pygame.image.load('monsters/' + spritedir + '/' + prefix + '_2.png'),
				pygame.image.load('monsters/' + spritedir + '/' + prefix + '_3.png')
			]
		}
