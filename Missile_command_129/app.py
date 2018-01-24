import pygame
import random
import math

pygame.init()

display_width = 600
display_height = 600

black = (0,0,0)
white = (255,255,255)

gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption("Missile Command")

clock = pygame.time.Clock()

crashed = False

explosion_radius = 25

LAUNCH_MISSILE = pygame.USEREVENT+1
pygame.time.set_timer(LAUNCH_MISSILE, 2000)


class antimissileClass():
	def __init__(self, gameDisplay, target):
		self.gameDisplay = gameDisplay
		self.width = self.gameDisplay.get_width()
		self.height = self.gameDisplay.get_height()
		self.progress = 0
		self.startx = self.width/2
		self.starty = self.height
		self.endx = target[0]
		self.endy = target[1]
		self.boom = False

	def update(self):
		if(self.startx > self.endx):
			pygame.draw.aaline(
				self.gameDisplay, 
				(0,0,255), 
				[self.startx,self.starty], 
				[
					self.startx + ((self.endx - self.startx) * self.progress),
					self.starty  - (self.starty - self.endy)* self.progress
				],
				1
			)
		else:
			pygame.draw.aaline(
				self.gameDisplay, 
				(255, 0, 0), 
				[self.startx,self.starty], 
				[
					self.startx + ((self.endx - self.startx) * self.progress),
					self.starty  - (self.starty - self.endy)* self.progress
				],
				1
			)

		if (self.progress < 1):
			self.progress += 0.04
		else:
			self.boom = True

class missileClass():
	def __init__(self, gameDisplay):
		self.width = display_width
		self.height = display_height
		self.gameDisplay = gameDisplay
		self.progress = 0
		self.startx = random.randint(2,self.width -2)
		self.starty = 0
		self.endx = random.randint(2,self.width -2)
		self.endy = self.height
		self.boom = False
		self.posx = 0
		self.posy = 0

	def update(self):
		if(self.startx > self.endx):
			pygame.draw.aaline(self.gameDisplay, (0,0,255), [self.startx,self.starty], [self.startx + ((self.endx - self.startx) * self.progress), self.endy * self.progress], 1)
			self.posx = self.startx + ((self.endx - self.startx) * self.progress)
			self.posy = self.endy * self.progress
		else:
			pygame.draw.aaline(self.gameDisplay, (255,0,0), [self.startx,self.starty], [self.endx + ((self.startx - self.endx) * (1 - self.progress)), self.endy * self.progress], 1)
			self.posx = self.endx + ((self.startx - self.endx) * (1 - self.progress))
			self.posy = self.endy * self.progress

		if (self.progress < 1):
			self.progress += 0.004
		else:
			self.boom = True

class explosionClass():
	def __init__(self, gameDisplay, pos):
		self.width = display_width
		self.height = display_height
		self.gameDisplay = gameDisplay
		self.progress = 0
		self.posx = pos[0]
		self.posy = pos[1]
		self.boom = False

	def update(self):
		pygame.draw.circle(self.gameDisplay, (0,0,255), [self.posx, self.posy], explosion_radius, 0)
		
		if (self.progress < 1):
			self.progress += 0.05
		else:
			self.boom = True

def colision(explosionQueue, missileQueue):
	for missile_index, missile in enumerate(missileQueue):
		for explosion_index, explosion in enumerate(explosionQueue):
			if (math.hypot(explosion.posx - missile.posx, explosion.posy - missile.posy ) < explosion_radius):
				missileQueue.pop(missile_index)

missileQueue = []
antiMissileQueue = []
explosionQueue = []

while not crashed:
	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			crashed = True
			print(event)
		if(event.type == LAUNCH_MISSILE):
			missileQueue.append(missileClass(gameDisplay))
			print(event)
		if(event.type == pygame.MOUSEBUTTONDOWN):
			antiMissileQueue.append(antimissileClass(gameDisplay, event.pos))
			print(event)
	
	gameDisplay.fill(white)

	colision(explosionQueue, missileQueue)

	for index, missile in enumerate(missileQueue):
		if(missile.boom == True):
			missileQueue.pop(index)
		missile.update()

	for index, antiMissile in enumerate(antiMissileQueue):
		if(antiMissile.boom == True):
			explosionQueue.append(explosionClass(gameDisplay,(antiMissile.endx,antiMissile.endy)))
			antiMissileQueue.pop(index)
		antiMissile.update()

	for index, explosion in enumerate(explosionQueue):
		if(explosion.boom == True):
			explosionQueue.pop(index)
		explosion.update()


	pygame.display.update()

	clock.tick(30)

pygame.quit()
quit()
