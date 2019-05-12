import numpy as np
import random
import pygame as pg
from random import randrange
size = 10
for x in range(size):
    position = pg.math.Vector2(1, 2)
    velolicty = pg.math.Vector2(8, 0).rotate(random.randrange(360))
    position += velolicty
    print position



n = 10

empty_list = [ [] for i in range(n) ]

