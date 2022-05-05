import pygame
from monster import Monster
from egg import Egg
from monster_data import MonsterData
from room import Room
from solar import Solar
from evo_overlay import EvoOverlay

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

room = Room('bg/beetleland.png',[0,176],[46,96])
bg = room.bg

solar = Solar()
evo_overlay = EvoOverlay()

savefile = open("savefile","r")
saves = savefile.read().split(",")
savefile.close()

if "Egg" in saves[0]:
	mainMonster = Egg(MonsterData(saves[0]),room)
else:
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

	if mainMonster.age >= mainMonster.lifespan:

		next_monster = mainMonster.monster_data.get_next_monster()
		cur_x = mainMonster.rect.x
		cur_y = mainMonster.rect.y

		if "Egg" in next_monster:
			mainMonster = Egg(MonsterData(next_monster),room)
		else:
			mainMonster = Monster(MonsterData(next_monster),room)

		mainMonster.rect.x = cur_x
		mainMonster.rect.y = cur_y


	mainMonster.update()

	evo_overlay.update()

	solar.update()

	with open("savefile","w") as save:
		save.write(mainMonster.monster_data.name + ',')
		save.write(str(mainMonster.age))

	screen.blit(bg,(0,0))

	shadow = mainMonster.surf.copy()
	shadow.fill((0,0,0,175),None,pygame.BLEND_RGBA_MULT)


	screen.blit(pygame.transform.smoothscale(shadow,(solar.shadow_w,16)),mainMonster.rect.move(solar.shadow_dx,48))
	screen.blit(mainMonster.surf,mainMonster.rect)

	screen.fill(solar.get_tint(),None,pygame.BLEND_RGBA_MIN)

	screen.blit(evo_overlay.get_sprite(),evo_overlay.rect)

	pygame.display.flip()

	clock.tick(60)

