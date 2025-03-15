import pygame
from constants import *

class Enemy():

    all_enemies = []

    def __init__(self, x, y, speed,  path):
        self.all_enemies.append(self)
        self.x = x
        self.y = y
        self.path = path
        self.speed = speed
        self.sprite = pygame.image.load("images/enemy_sprites/grr.png")
        self.sprite = pygame.transform.scale(self.sprite, (TILE_SIZE, TILE_SIZE))
        self.current_direction = None
        self.directions_index = 0
        self.distance_travelled = 0

    def is_dead(self):
        if self.health <= 0:
            Enemy.all_enemies.remove(self)

    def move(self):
        if self.current_direction == "left":
            self.x -= self.speed
        elif self.current_direction == "right":
            self.x += self.speed
        elif self.current_direction == "up":
            self.y -= self.speed
        elif self.current_direction == "down":
            self.y += self.speed
        self.distance_travelled += self.speed
        
    def update(self):
        self.determine_direction()
        self.move()

    def determine_direction(self):
        if self.distance_travelled >= TILE_SIZE:
            if self.directions_index + 1 < len(self.path):
                self.directions_index += 1
                self.distance_travelled = 0
        self.current_direction = self.path[self.directions_index]

    def take_damage(self, damage):
        self.health -= damage

    def render(self, screen):
        screen.blit(self.sprite, (self.x, self.y))

class EnemyVariant1(Enemy):
    def __init__(self, x, y, health, damage, speed):
        super().__init__()
        self.x = x
        self.y = y
        self.health = health
        self.damage = damage
        self.speed = speed


        