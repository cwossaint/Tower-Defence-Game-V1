from entities.enemy.base_enemy_class import Enemy
from constants.global_constants import GRID_SIZE, RED
import pygame
import math

class Projectile():

    all_projectiles = []

    def __init__(self, x, y, target, damage, size=15, shape="circle", speed=15, color=RED):
        self.x = x
        self.y = y
        self.size = size
        self.shape = shape
        self.speed = speed
        self.color = color
        self.target = target
        self.damage = damage
        self.direction_x = None
        self.direction_y = None
        self.all_projectiles.append(self)

    def destroy(self):
        if self in Projectile.all_projectiles:
            Projectile.all_projectiles.remove(self)

    def render(self, screen):
        if self.shape == "circle":
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.size/2)

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
            self.check_collision()
            if self.past_grid():
                self.destroy()
        else:
            self.calculate_direction()

    def check_collision(self):
        for enemy in Enemy.all_enemies:
            if pygame.Rect.colliderect(self.rect, enemy.rect):
                    self.destroy()
                    enemy.take_damage(self.damage)
                    break


    def past_grid(self):
        if self.x > GRID_SIZE or self.x < 0 or self.y > GRID_SIZE or self.y < 0:
            return True
        