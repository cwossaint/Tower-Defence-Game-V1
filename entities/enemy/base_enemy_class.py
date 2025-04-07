from constants import TILE_SIZE
import pygame


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

    def update(self):
        self.determine_direction()
        self.move()
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
        
    def get_slowed(self, percentage_slow):
        self.speed -= self.speed * percentage_slow
            
    def attack_base(self):
        self.remove()
        self.game_data.remove_lives(self.damage)

    def take_damage(self, damage):
        self.health -= damage

    def render(self, screen):
        screen.blit(self.sprite, (self.x, self.y))

    def scale_stats(self):
        self.health *= (1.25 ** self.wave) //1 
        self.damage *= (1.05 ** self.wave) //1 
        self.speed *= (1.05 ** self.wave) //1

