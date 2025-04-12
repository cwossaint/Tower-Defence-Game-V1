import pygame
from constants.global_constants import TILE_SIZE

def load_and_scale_image(image_path):
    image = pygame.image.load(image_path)
    return pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))

# Loading enemy sprites
BASEENEMYSPRITE = load_and_scale_image("images/enemy_sprites/base.png")
BOSSENEMYSPRITE = load_and_scale_image("images/enemy_sprites/boss.png")
SPEEDYENEMYSPRITE = load_and_scale_image("images/enemy_sprites/speedy.png")
TANKYENEMYSPRITE = load_and_scale_image("images/enemy_sprites/tanky.png")

# Loading tower sprites
DARTTOWERSPRITE = load_and_scale_image("images/tower_sprites/dart_tower.png")
BOOMERANGTOWERSPRITE = load_and_scale_image("images/tower_sprites/boomerang_tower.png")
CANNONTOWERSPRITE = load_and_scale_image("images/tower_sprites/cannon_tower.png")
GLUETOWERSPRITE = load_and_scale_image("images/tower_sprites/glue_tower.png")
GATLINGTOWERSPRITE = load_and_scale_image("images/tower_sprites/gatling_tower.png")
