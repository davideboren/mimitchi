import pygame
from monster import Monster
from monster_data import MonsterData
from room import Room

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT
)


SCREEN_WIDTH = 240
SCREEN_HEIGHT = 160

pygame.init()

pygame.display.set_caption("Mimitchi")

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

room = Room('bg/grid.png',[0,176],[46,96])
bg = room.bg

mainMonster = Monster(MonsterData('blobby'),room)

clock = pygame.time.Clock()

running = True

while running:
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				running = False
		elif event.type == QUIT:
			running = False

	mainMonster.update()

	screen.blit(bg,(0,0))

	screen.blit(mainMonster.surf,mainMonster.rect)

	pygame.display.flip()

	clock.tick(60)
