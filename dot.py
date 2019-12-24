import pygame
import brian
import numpy as np
class dot:

    Dead = False
    Goal = False
    def __init__(self, size ):
        self.size = size
        self.pos = np.array([400,800])
        self.vel = np.array([0,0])
        self.acc = np.array([0,0])

    # determine dot move and checks if it hits goal, boundry or object

    def DotMove(self):
        step = 0
        #self.pos[1] = self.pos[1]-107 # making some semirandom arbritary movement
        #self.pos[0] = self.pos[0] + self.pos[1]/20
        print step
        step = step + 1
        Directions = brian.brian()
        Directions.Random()
        self.pos = Directions.position[0][:]
        #checking hitting enything.
        if self.pos[1] == 0 and self.pos[0] == 400:
            self.Goal = True 
        elif self.pos[0] < 0 or self.pos[0] > 800:
            self.Dead = True
        elif self.pos[1] < 0 or self.pos[1] > 800:
            self.Dead = True

    # calculates the fitness of dot. Fitness is the difference in landed spot and goal spot    

    def fitness(self):
        fitness = self.pos[0]-400
        print(fitness)
        print(self.pos[1])
        print(self.pos[0]) 

    # printing dot to screen

    def PrintDot(self, screen):
        pygame.draw.circle(screen,(0,0,0), (self.pos[0],self.pos[1]), (self.size))


