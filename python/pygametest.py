import sys, pygame

from pygame.locals import*
pygame.init()

size = width, height = 320, 240
speed = 5
black = 0,0,0
radius = 10
ballpos = [70,20]
screen = pygame.display.set_mode(size)

pygame.display.set_caption('my first game')

while True:
	pygame.time.delay(100)
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
	
	
	keys = pygame.key.get_pressed()
	if keys[pygame.K_UP] and ballpos[0] > 0 + radius :
		ballpos[0] -= speed
	if keys[pygame.K_DOWN] and ballpos[0] < height - radius:
		ballpos[0] += speed
	if keys[pygame.K_LEFT] and ballpos[1] > 0 + radius:
		ballpos[1] -= speed
	if keys[pygame.K_RIGHT] and ballpos[1] < width - radius:
		ballpos[1] += speed	


	if ballpos[0] in range(90,240) and ballpos[1] in range(210 - radius  ,220 + radius ):
		pygame.quit()
		sys.exit()


	screen.fill((255,255,255))

	wall  = pygame.draw.rect(screen, (0,0,0), (200,90,20,150))
	wall2 = pygame.draw.rect(screen, (0,0,0), (100,0,20,150))
	
	ball = pygame.draw.circle(screen, (0,0,0), (ballpos[1],ballpos[0]), radius)
	goal = pygame.draw.circle(screen, (0,255,0),(width,height/2), radius)

	pygame.display.update()	
 


