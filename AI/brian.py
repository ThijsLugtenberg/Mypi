import numpy as np
import random
from pygame.math import Vector2

class brian:
        

    def __init__(self):
        self.size = 1000 
        #directions = [ [] in range (self.size)]
        self.position = np.zeros((self.size,2)) 
        self.Random()
    def Random(self):
        #self.position = np.array((self.size,2))
        self.position[0][0] = 400
        self.position[0][1] = 800
        for x in range (self.size):
          randx = random.randrange(-10,10)
          randy = random.randrange(-10,10)
          self.position[x][0] = self.position[x-1][0] + randx
          self.position[x][1] = self.position[x-1][1] + randy
          self.position[0][0] = 400
          self.position[0][1] = 750 
          self.position = self.position.astype(int)
         # print self.position.shape
    def mutate(self):
        mutationRate = 0.01 

        rand = random(1)

        if rand > mutationRate:
            RandomAngle = random(2*PI)
            directions[i] = pg.math.Vector2(RandomAngle)
        
        
