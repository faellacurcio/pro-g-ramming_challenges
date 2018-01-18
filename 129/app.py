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

class missileClass():
	def __init__(self, gameDisplay):
		self.width = display_width
		self.height = display_height
		self.gameDisplay = gameDisplay
		self.progress = 0
		self.start = random.randint(2,self.width -2)
		self.end = random.randint(2,self.width -2)

	def update(self):
		if(self.start > self.end):
			pygame.draw.aaline(self.gameDisplay, (0,0,255), [self.start,0], [self.start + ((self.end - self.start) * self.progress), display_height * self.progress], 1)
		else:
			pygame.draw.aaline(self.gameDisplay, (255,0,0), [self.start,0], [self.end + ((self.start - self.end) * (1 - self.progress)), display_height * self.progress], 1)

		if (self.progress < 1):
			self.progress += 0.01

		# Draw the missile

missileQueue = []

while not crashed:
	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			crashed = True
		if(event.type == pygame.KEYDOWN):
			missileQueue.append(missileClass(gameDisplay))

		print(event)
	
	gameDisplay.fill(white)
	# pygame.draw.line(gameDisplay, black, (0,0), (100,100), width=1)

	for missile in missileQueue:
		missile.update()

	pygame.display.update()

	clock.tick(30)

pygame.quit()
quit()
