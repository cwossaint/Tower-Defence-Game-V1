import pygame
from constants import *
from entities.Projectile import *

class Enemy():

    all_enemies = []

    def __init__(self, x, y, health, speed, directions_list, game_data):
        self.all_enemies.append(self)
        self.game_data = game_data
        self.x = x
        self.y = y
        self.health = health
        self.directions_list = directions_list
        self.damage = 10
        self.speed = speed
        self.sprite = pygame.image.load("images/enemy_sprites/grr.png")
        self.rect = pygame.Rect(self.x, self.y, self.sprite.get_width(), self.sprite.get_height())
        self.sprite = pygame.transform.scale(self.sprite, (TILE_SIZE, TILE_SIZE))
        self.current_direction = None
        self.directions_index = 0
        self.distance_travelled = 0

    def is_dead(self):
        if self.health <= 0:
            if self in Enemy.all_enemies: 
                Enemy.all_enemies.remove(self)
                self.game_data.add_cash(10)
            return True

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
        self.rect = pygame.Rect(self.x, self.y, self.sprite.get_width(), self.sprite.get_height())

    def check_collision(self):
        for projectile in Projectile.all_projectiles:
            if pygame.Rect.colliderect(self.rect, projectile.rect):
                projectile.destroy()
                self.take_damage(projectile.damage)

    def update(self):
        self.determine_direction()
        self.move()
        self.check_collision()

    def determine_direction(self):
        if self.distance_travelled >= TILE_SIZE:
            if not self.end_of_path():
                self.directions_index += 1
                self.distance_travelled = 0
        self.current_direction = self.directions_list[self.directions_index]

    def end_of_path(self):
        if self.directions_index + 1 < len(self.directions_list):
            return False
        else: 
            self.attack_base()
            return True
            
    def attack_base(self):
        if self in Enemy.all_enemies: 
            Enemy.all_enemies.remove(self)
            self.game_data.remove_lives(self.damage)

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


        