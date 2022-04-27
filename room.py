import pygame

class Room():
	def __init__(self,bg_path,boundx,boundy):
		self.bg = pygame.image.load(bg_path)
		self.boundx = boundx
		self.boundy = boundy
