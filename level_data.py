import pygame
from constants import *

LEVEL1MAPSPRITE = pygame.image.load("images/test_map.png")
LEVEL1MAPSPRITE = pygame.transform.scale(LEVEL1MAPSPRITE, (SCREEN_WIDTH, SCREEN_HEIGHT))

LEVEL1MAPARRAY =   [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [1, 1, 1, 0, 0, 0, 0, 2, 0, 0],
                    [0, 0, 1, 0, 2, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 1, 0, 0, 2, 0],
                    [2, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 1, 1, 1, 3],
                    [0, 0, 2, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 2, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]