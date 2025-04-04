import pygame
from entities.enemy_sprites import *
from entities.Projectile import *

class Enemy():

    all_enemies = []

    def __init__(self, x, y, directions_list, game_data, wave, health, damage, speed):
        self.x = x
        self.y = y
        self.health = health
        self.damage = damage
        self.speed = speed
        self.all_enemies.append(self)
        self.game_data = game_data
        self.directions_list = directions_list
        self.current_direction = None
        self.directions_index = 0
        self.distance_travelled = 0
        self.wave = wave
        self.removed = False

    def check_is_dead(self):
        if self.health <= 0:
            self.remove()
            self.game_data.add_cash(self.value)

    def remove(self):
        if self in Enemy.all_enemies: 
            Enemy.all_enemies.remove(self)
            self.removed = True

    def calculate_distance(self):
        if  self.distance_travelled + self.speed  > TILE_SIZE:
            distance = TILE_SIZE - self.distance_travelled
        else:
            distance = self.speed
        return distance

    def move(self):
        distance = self.calculate_distance()
        if self.current_direction == "left":
            self.x -= distance
        elif self.current_direction == "right":
            self.x += distance
        elif self.current_direction == "up":
            self.y -= distance
        elif self.current_direction == "down":
            self.y += distance
        self.distance_travelled += distance
        self.update_rect()

    def update_rect(self):
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
        self.check_is_dead()

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
        self.remove()
        self.game_data.remove_lives(self.damage)

    def take_damage(self, damage):
        self.health -= damage

    def render(self, screen):
        screen.blit(self.sprite, (self.x, self.y))

    def scale_stats(self):
        self.health *= (1.1 ** self.wave) //1 
        self.damage *= (1.1 ** self.wave) //1 
        self.speed *= (1.05 ** self.wave) //1


class Tanky(Enemy):
    def __init__(self, x, y, directions_list, game_data, wave, health=50, damage=20, speed=3):
        super().__init__(x, y, directions_list, game_data, wave, health, damage, speed)
        self.sprite = TANKYENEMYSPRITE
        self.rect = pygame.Rect(self.x, self.y, self.sprite.get_width(), self.sprite.get_height())
        self.value = 10
        self.scale_stats()
        print("Tanky health" + str(self.health))
        print("Tanky speed: " + str(self.speed))
        print("Tanky damage: " + str(self.damage))

class Speedy(Enemy):
    def __init__(self, x, y, directions_list, game_data, wave, health=15, damage=10, speed=10):
        super().__init__(x, y, directions_list, game_data, wave, health, damage, speed)
        self.sprite = SPEEDYENEMYSPRITE
        self.rect = pygame.Rect(self.x, self.y, self.sprite.get_width(), self.sprite.get_height())
        self.value = 5
        self.scale_stats()
        print("Speedy speed: " + str(self.speed))
        print("Speedy Health: " + str(self.health))
        print("Speedy damage: " + str(self.damage))

class Basic(Enemy):
    def __init__(self, x, y, directions_list, game_data, wave, health=20, damage=10, speed=5):
        super().__init__(x, y, directions_list, game_data, wave, health, damage, speed)
        self.sprite = BASEENEMYSPRITE
        self.rect = pygame.Rect(self.x, self.y, self.sprite.get_width(), self.sprite.get_height())
        self.value = 2
        self.scale_stats()
        print("basic health" + str(self.health))
        print("basci speed: " + str(self.speed))
        print("basic damage: " + str(self.damage))

class Boss(Enemy):
    def __init__(self, x, y, directions_list, game_data, wave, health=500, damage=100, speed=4):
        super().__init__(x, y, directions_list, game_data, wave, health, damage, speed)
        self.sprite = BOSSENEMYSPRITE
        self.rect = pygame.Rect(self.x, self.y, self.sprite.get_width(), self.sprite.get_height())
        self.value = 100
        self.scale_stats()
        print("Boss health" + str(self.health))
        print("Boss speed: " + str(self.speed))
        print("Boss damage: " + str(self.damage))

        