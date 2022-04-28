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
		if '_' in sprites[0]:
			prefix = sprites[0].split('_')[0]
		else:
			prefix = sprites[1].split('_')[0]


		if len(sprites) == 13:
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
					pygame.image.load('monsters/' + spritedir + '/' + prefix + '_9.png')
				]
			}

		elif len(sprites) <= 6:
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

