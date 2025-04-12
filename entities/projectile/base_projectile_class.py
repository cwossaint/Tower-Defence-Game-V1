from entities.enemy.base_enemy_class import Enemy
from constants.global_constants import GRID_SIZE, RED
import pygame
import math

class Projectile():

    all_projectiles = []  # Class-level list to track all active projectiles

    def __init__(self, x, y, target, damage, size=15, shape="circle", speed=15, color=RED):
        # Initialize projectile properties
        self.x = x  # Current x position
        self.y = y  # Current y position
        self.size = size  # Diameter of the projectile
        self.shape = shape  # Shape for rendering (circle, etc.)
        self.speed = speed  # Movement speed per update
        self.color = color  # Color used in rendering
        self.target = target  # Target coordinates (x, y)
        self.damage = damage  # Damage dealt to enemy on hit
        self.direction_x = None  # Normalized x direction
        self.direction_y = None  # Normalized y direction
        self.all_projectiles.append(self)  # Add to global list of projectiles

    def destroy(self):
        # Remove projectile from active list
        if self in Projectile.all_projectiles:
            Projectile.all_projectiles.remove(self)

    def render(self, screen):
        # Draw the projectile on the screen
        if self.shape == "circle":
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.size/2)

    def calculate_direction(self):
        # Calculate normalized direction vector toward the target
        targetx, targety = self.target
        if self.target:
            dx, dy = targetx - self.x, targety - self.y
            distance = math.sqrt(dx ** 2 + dy ** 2)
            self.direction_x = dx / distance
            self.direction_y = dy / distance

    def move_towards_target(self):
        # Move the projectile toward the target each frame
        self.x += self.direction_x * self.speed
        self.y += self.direction_y * self.speed
        self.update_rect()

    def update_rect(self):
        # Update the hitbox for collision detection
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def update(self):
        # Called each frame to update projectile state
        if self.direction_x or self.direction_y:
            self.move_towards_target()
            self.check_collision()
            if self.past_grid():
                self.destroy()
        else:
            self.calculate_direction()

    def check_collision(self):
        # Check if the projectile has hit any enemy
        for enemy in Enemy.all_enemies:
            if pygame.Rect.colliderect(self.rect, enemy.rect):
                self.destroy()
                enemy.take_damage(self.damage)
                break

    def past_grid(self):
        # Check if projectile has gone outside the playable area
        if self.x > GRID_SIZE or self.x < 0 or self.y > GRID_SIZE or self.y < 0:
            return True
