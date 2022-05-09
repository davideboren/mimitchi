import pygame
class EvoOverlay(pygame.sprite.Sprite):
	def __init__(self):
		self.frame_counter = 0
		self.x_interval = 16
		self.width = 240
		self.height = 160

		self.mode = "none"
		self.rolled_in = False

		self.counter = 0

		self.sprite = pygame.image.load("../gfx/evo_overlay.png")
		self.rect = pygame.Rect(0,0,0,self.height)
		
	def update(self):

		if self.frame_counter >= 15:

			if self.mode == "roll_in":
				if self.rect.width < self.width:
					self.rect.width += self.x_interval
				else:
					self.rolled_in = True
					self.mode = "roll_out"

			elif self.mode == "roll_out":
				if self.rect.left < self.width:
					self.rect.left += self.x_interval
					self.sprite = pygame.transform.flip(self.sprite,False,True)
				else:
					self.rect = pygame.Rect(0,0,0,self.height)
					self.mode = "none"
					self.rolled_in = False

			self.sprite = pygame.transform.flip(self.sprite,False,True)
			self.frame_counter = 0

		self.frame_counter +=1
	
	def get_sprite(self):
		surf = pygame.Surface((self.rect.width,self.rect.height))
		surf.blit(self.sprite,(0,0))
		return surf
