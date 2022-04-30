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

savefile = open("savefile","r")
saves = savefile.read().split(",")
savefile.close()

mainMonster = Monster(MonsterData(saves[0]),room)
mainMonster.age = int(saves[1])

clock = pygame.time.Clock()

running = True

while running:
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				running = False
		elif event.type == QUIT:
			running = False

	if mainMonster.age > mainMonster.lifespan:
		mainMonster.evolve(MonsterData(mainMonster.monster_data.get_next_monster()))

	mainMonster.update()

	with open("savefile","w") as save:
		save.write(mainMonster.monster_data.name + ',')
		save.write(str(mainMonster.age))

	screen.blit(bg,(0,0))

	#Don't know how much I like this. Will probably change it.
	shadow = mainMonster.surf.copy()
	shadow.fill((25,25,25,200),None,pygame.BLEND_RGBA_MULT)

	screen.blit(pygame.transform.scale(shadow,(80,16)),mainMonster.rect.move(-8,52))
	screen.blit(mainMonster.surf,mainMonster.rect)

	pygame.display.flip()

	clock.tick(60)

