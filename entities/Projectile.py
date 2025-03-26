import math
import pygame
from constants import *
from entities.projectile_data import *

class Projectile():

    all_projectiles = []

    def __init__(self, x, y, target, damage, type) -> None:
        self.x = x
        self.y = y
        self.type = type
        self.size = None
        self.rect = None
        self.sprite = None
        self.shape = None
        self.speed = None
        self.color = None
        self.target = target
        self.damage = damage
        self.direction_x = None
        self.direction_y = None
        self.set_attrbiutes()
        self.all_projectiles.append(self)



    def set_attrbiutes(self):
        projectile_type_data = PROJECTILE_DATA.get(self.type)
        self.size = projectile_type_data.get("size")
        self.speed = projectile_type_data.get("speed")
        self.shape = projectile_type_data.get("shape")
        self.color = projectile_type_data.get("color")
        self.sprite = projectile_type_data.get("sprite")
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)


    def destroy(self):
        Projectile.all_projectiles.remove(self)

    def render(self, screen):
        if self.shape == "circle":
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.size/2)
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
