import pygame
import random

pygame.init()

display_width = 600
display_height = 600

black = (0,0,0)
white = (255,255,255)

gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption("Missile Command")

clock = pygame.time.Clock()

crashed = False

class antimissileClass():
	def __init__(self, gameDisplay, target):
		self.width = display_width
		self.height = display_height
		self.gameDisplay = gameDisplay
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
			self.progress += 0.03
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

	def update(self):
		if(self.startx > self.endx):
			pygame.draw.aaline(self.gameDisplay, (0,0,255), [self.startx,self.starty], [self.startx + ((self.endx - self.startx) * self.progress), self.endy * self.progress], 1)
		else:
			pygame.draw.aaline(self.gameDisplay, (255,0,0), [self.startx,self.starty], [self.endx + ((self.startx - self.endx) * (1 - self.progress)), self.endy * self.progress], 1)

		if (self.progress < 1):
			self.progress += 0.01
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
		pygame.draw.circle(self.gameDisplay, (0,0,255), [self.posx, self.posy], 25, 0)
		
		if (self.progress < 1):
			self.progress += 0.05
		else:
			self.boom = True


missileQueue = []
antiMissileQueue = []
explosionQueue = []

while not crashed:
	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			crashed = True
		if(event.type == pygame.KEYDOWN):
			missileQueue.append(missileClass(gameDisplay))
		if(event.type == pygame.MOUSEBUTTONDOWN):
			antiMissileQueue.append(antimissileClass(gameDisplay, event.pos))
		print(event)
	
	gameDisplay.fill(white)
	# pygame.draw.line(gameDisplay, black, (0,0), (100,100), width=1)

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
