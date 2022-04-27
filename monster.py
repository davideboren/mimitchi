import pygame
from random import randint

class Monster(pygame.sprite.Sprite):
	def __init__(self,monster_data,room):
		super(Monster,self).__init__()
		self.frame_counter = 0
		self.framerate = 60
		self.monster_data = monster_data
		self.room = room

		self.mode = "walk"
		self.mode_timer = 0
		self.mode_duration = randint(2,14)
		self.currentframe = 0
		self.currentsprite = self.monster_data.spritedict[self.mode][self.currentframe]
		self.surf = self.currentsprite
		self.rect = self.surf.get_rect()

		self.rect.x = 100
		self.rect.y = 90

		self.facing_right = True

		self.destx = randint(room.boundx[0],room.boundx[1])
		self.desty = randint(room.boundy[0],room.boundy[1])

	def update(self):
		#Only update sprite twice per second
		if self.frame_counter >= self.framerate/2:
			
			self.currentframe = self.currentframe ^ 1
			self.currentsprite = self.monster_data.spritedict[self.mode][self.currentframe]

			self.frame_counter = 0

			if self.mode == "stand":
				if self.mode_timer > 10:
					self.set_rand_dest()
					self.mode_timer = 0
					self.mode_duration = randint(2,14)
				self.mode_timer += 1

		self.surf = pygame.transform.flip(self.currentsprite,self.facing_right,False)

		if self.mode == "walk" and self.frame_counter % 2:
			self.step_toward_dest()
	
		self.frame_counter += 1

	def step_toward_dest(self):
		dx = 0      
		dy = 0

		distx = self.destx - self.rect.x
		disty = (self.desty - self.rect.y)

		if(distx or disty):
			if distx:
				dx = distx/abs(distx)
				self.facing_right = dx > 0
			if disty and self.frame_counter % 3 == 0:
				dy = disty/abs(disty)

			self.rect.move_ip(dx,dy)
		else:
			self.mode = "stand"


	def set_rand_dest(self):
		self.destx = randint(self.room.boundx[0],self.room.boundx[1])
		self.desty = randint(self.room.boundy[0],self.room.boundy[1])
		self.mode = "walk"
