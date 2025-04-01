import pygame
from constants import *

BASEENEMYSPRITE = pygame.image.load("images/enemy_sprites/base.png")
BASEENEMYSPRITE = pygame.transform.scale(BASEENEMYSPRITE, (TILE_SIZE, TILE_SIZE))

BOSSENEMYSPRITE = pygame.image.load("images/enemy_sprites/boss.png")
BOSSENEMYSPRITE = pygame.transform.scale(BOSSENEMYSPRITE, (TILE_SIZE, TILE_SIZE))

SPEEDYENEMYSPRITE = pygame.image.load("images/enemy_sprites/speedy.png")
SPEEDYENEMYSPRITE = pygame.transform.scale(SPEEDYENEMYSPRITE, (TILE_SIZE, TILE_SIZE))

TANKYENEMYSPRITE = pygame.image.load("images/enemy_sprites/tanky.png")
TANKYENEMYSPRITE = pygame.transform.scale(TANKYENEMYSPRITE, (TILE_SIZE, TILE_SIZE))