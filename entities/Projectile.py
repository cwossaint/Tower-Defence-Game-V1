import math
import pygame
from constants import *

class Projectile():

    all_projectiles = []

    def __init__(self, x, y, target, damage) -> None:
        self.x = x
        self.y = y
        self.size = 50
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
        self.target = target
        self.sprite = None
        self.damage = damage
        self.direction_x = None
        self.direction_y = None
        self.speed = 20
        self.all_projectiles.append(self)

    def destroy(self):
        Projectile.all_projectiles.remove(self)

    def render(self, screen):
        pygame.draw.circle(screen, RED, (self.x, self.y), self.size/2)
        #screen.blit(self.sprite, (self.x, self.y))

    def calculate_direction(self):
        targetx, targety = self.target
        if self.target:
            dx, dy = targetx - self.x, targety - self.y
            distance = math.sqrt(dx ** 2 + dy ** 2)
            self.direction_x = dx / distance
            self.direction_y = dy/ distance

    def move_towards_target(self):
            self.x += self.direction_x * self.speed
            self.y += self.direction_y * self.speed
            self.update_rect()
            
    def update_rect(self):
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def update(self):
        if self.direction_x or self.direction_y:
            self.move_towards_target()
            if self.past_grid():
                self.destroy()
        else:
            self.calculate_direction()

    def past_grid(self):
        if self.x > GRID_SIZE or self.x < 0 or self.y > GRID_SIZE or self.y < 0:
            return True
