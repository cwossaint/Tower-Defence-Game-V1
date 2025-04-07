from constants.global_constants import TILE_SIZE
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
        self.slow_debuff = 0
        self.slow_debuff_timer = 0
        self.slow_duration = 0
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
        distance_to_travel = self.speed - (self.speed * self.slow_debuff)
        if  self.distance_travelled + distance_to_travel  > TILE_SIZE:
            distance = TILE_SIZE - self.distance_travelled
        else:
            distance = distance_to_travel
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
        self.check_slow()

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
        
    def get_slowed(self, percentage_slow, slow_duration):
        if self.slow_debuff == 0:
            self.slow_debuff = percentage_slow
            self.slow_duration = slow_duration
            self.slow_debuff_timer = 0

    def check_slow(self):
        if self.slow_debuff > 0:
            if self.slow_debuff_timer > self.slow_duration:
                self.slow_debuff = 0
            else: 
                self.slow_debuff_timer += 1
            
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

