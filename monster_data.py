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
import json
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

		with open('monsters/Tamagotchi_PS1/sprite_sheet_atlas.json','r') as f:
			self.atlas = json.load(f)

		self.sprite_sheet = pygame.image.load('monsters/' + spritedir + '/sprite_sheet.png')
		self.bg_color = self.sprite_sheet.get_at((0,0))


	def get_sprite(self,mode,frame):
		rect = pygame.Rect(\
			self.atlas["coords"][mode][str(frame)][0],\
			self.atlas["coords"][mode][str(frame)][1],\
			self.atlas["sprite_w"],\
			self.atlas["sprite_h"])
		surf = pygame.Surface((64,64))
		surf.fill(self.bg_color)
		surf.blit(self.sprite_sheet,(8,16),rect)
		surf.set_colorkey(self.bg_color)
		return surf.convert_alpha()

	def get_next_monster(self):
		sel = randint(0,len(self.evo_list)-1)
		return self.evo_list[sel]
