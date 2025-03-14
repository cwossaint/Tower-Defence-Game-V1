import math
import pygame

class Projectile():

    all_projectiles = []

    def __init__(self, x, y, target, damage) -> None:
        self.x = x
        self.y = y
        self.target = target
        self.sprite = pygame.image
        self.damage = damage
        self.speed = 10
        self.all_projectiles.append(self)

    def destroy(self):
        self.all_projectiles.remove(self)

    def render(self, screen):
        screen.blit(self.sprite, (self.x, self.y))

    def move_towards_target(self):
        targetx, targety = self.target
        if self.target:
            dx, dy = targetx - self.x, targety - self.y
            distance = math.sqrt(dx ** 2 + dy ** 2)
            self.x += (dx / distance) * self.speed
            self.y += (dy / distance) * self.speed

    def update(self):
        if self.active:
            self.move_towards_target()