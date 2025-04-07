import pygame
from constants import TILE_SIZE

BASEENEMYSPRITE = pygame.image.load("images/enemy_sprites/base.png")
BASEENEMYSPRITE = pygame.transform.scale(BASEENEMYSPRITE, (TILE_SIZE, TILE_SIZE))

BOSSENEMYSPRITE = pygame.image.load("images/enemy_sprites/boss.png")
BOSSENEMYSPRITE = pygame.transform.scale(BOSSENEMYSPRITE, (TILE_SIZE, TILE_SIZE))

SPEEDYENEMYSPRITE = pygame.image.load("images/enemy_sprites/speedy.png")
SPEEDYENEMYSPRITE = pygame.transform.scale(SPEEDYENEMYSPRITE, (TILE_SIZE, TILE_SIZE))

TANKYENEMYSPRITE = pygame.image.load("images/enemy_sprites/tanky.png")
TANKYENEMYSPRITE = pygame.transform.scale(TANKYENEMYSPRITE, (TILE_SIZE, TILE_SIZE))

DARTTOWERSPRITE = pygame.image.load("images/tower_sprites/dart_tower.png")
DARTTOWERSPRITE = pygame.transform.scale(DARTTOWERSPRITE, (TILE_SIZE, TILE_SIZE))

BOOMERANGTOWERSPRITE = pygame.image.load("images/tower_sprites/boomerang_tower.png")
BOOMERANGTOWERSPRITE = pygame.transform.scale(BOOMERANGTOWERSPRITE, (TILE_SIZE, TILE_SIZE))

CANNONTOWERSPRITE = pygame.image.load("images/tower_sprites/cannon_tower.png")
CANNONTOWERSPRITE = pygame.transform.scale(CANNONTOWERSPRITE, (TILE_SIZE, TILE_SIZE))

GLUETOWERSPRITE = pygame.image.load("images/tower_sprites/glue_tower.png")
GLUETOWERSPRITE = pygame.transform.scale(GLUETOWERSPRITE, (TILE_SIZE, TILE_SIZE))

GATLINGTOWERSPRITE = pygame.image.load("images/tower_sprites/gatling_tower.png")
GATLINGTOWERSPRITE = pygame.transform.scale(GATLINGTOWERSPRITE, (TILE_SIZE, TILE_SIZE))


