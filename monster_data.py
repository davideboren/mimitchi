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
		self.currentdir = 'monsters/' + spritedir
		self.atlas_filename = 'sprite_sheet_atlas.json'

		self.evo_list = []

		evo_file = open(self.currentdir + '/evos.txt',"r")
		for m in evo_file:
			self.evo_list.append(m.split('\n')[0])

		#Check for sprite atlas override, otherwise use parent
		if exists(self.currentdir + '/' + self.atlas_filename):
			with open(self.currentdir + '/' + self.atlas_filename, 'r') as f:
				self.atlas = json.load(f)
		else:
			with open(self.currentdir + '/../' + self.atlas_filename, 'r') as f:
				self.atlas = json.load(f)

		self.sprite_sheet = pygame.image.load(self.currentdir + '/sprite_sheet.png')
		self.bg_color = self.sprite_sheet.get_at((0,0))


	def get_sprite(self,mode,frame):
		rect = pygame.Rect(\
			self.atlas["coords"][mode][str(frame)][0],\
			self.atlas["coords"][mode][str(frame)][1],\
			self.atlas["sprite_w"],\
			self.atlas["sprite_h"])
		surf = pygame.Surface((64,64))
		surf.fill(self.bg_color)
		surf.blit(self.sprite_sheet,\
			( (64 - self.atlas["sprite_w"])/2, \
			64 - self.atlas["sprite_h"]), \
			rect)
		surf.set_colorkey(self.bg_color)
		return surf.convert_alpha()

	def get_next_monster(self):
		sel = randint(0,len(self.evo_list)-1)
		return self.evo_list[sel]

	def get_num_frames(self,mode):
		return len(self.atlas["coords"][mode])
