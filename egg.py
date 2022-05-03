import pygame
from random import randint

class Egg(pygame.sprite.Sprite):
	def __init__(self,monster_data,room):
		super(Egg,self).__init__()

		self.frame_counter = 0
		self.framerate = 60
		self.monster_data = monster_data
		self.room = room

		self.age = 0
		self.lifespan = 20

		self.mode = "stand"

		self.hatched = False

		self.currentframe = 0
		self.currentsprite = self.monster_data.get_sprite(self.mode,self.currentframe)
		self.surf = self.currentsprite
		self.rect = self.surf.get_rect()

		self.rect.x = 100
		self.rect.y = 90

	def update(self):

		if self.frame_counter >= self.framerate/2:

			if self.age == self.lifespan - self.monster_data.get_num_frames("hatch") + 1:
				self.set_mode("hatch")

			self.currentframe = (self.currentframe + 1) % self.monster_data.get_num_frames(self.mode)
			self.currentsprite = self.monster_data.get_sprite(self.mode,self.currentframe)

			self.frame_counter = 0

			self.age += 1

			
		self.surf = self.currentsprite

		self.frame_counter += 1

	def set_mode(self,mode):
		self.mode = mode
		self.mode_timer = 0

