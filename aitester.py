import sys, pygame, dot

from pygame.locals import *
pygame.init()

#Set up screen size en create display
size = 800, 800
screen = pygame.display.set_mode(size)

# set window caption
pygame.display.set_caption("AI tester")

# Create dot
#Dead = False
#Goal = False
TestDot = dot.dot(5)
# GoalDot = dot.dot(screen, 10, Dead, Goal)

while True:
    if TestDot.Dead == False and TestDot.Goal == False:
        pygame.time.delay(100)

        screen.fill((255,255,255))
        TestDot.DotMove()
        TestDot.PrintDot(screen)
        pygame.draw.circle(screen, (0,0,0), (400,0), 10)
        pygame.display.update()

    elif TestDot.Goal == True and TestDot.Dead == False:
        print ("Winner")
        TestDot.fitness()
        pygame.quit()
        sys.exit()
    elif TestDot.Dead == True and TestDot.Goal == False:
        print ("Loser")
        TestDot.fitness()
        pygame.quit()
        sys.exit()










        
