from entities.tower_sprites import *
from entities.enemy import *
from entities.Projectile import *
import math

class Tower():

    all_towers = []

    def __init__(self, x, y, range=100, damage=10, attack_delay=10):
        self.sprite = None
        self.range = None
        self.dmg = None
        self.cost = None
        self.range = range
        self.damage = damage
        self.attack_delay = attack_delay
        self.attack_delay = attack_delay
        self.attack_timer = 0
        self.x = x
        self.y = y
        self.target_coords = None
        self.target = None
        self.all_towers.append(self)

    def find_target(self):
        closest_enemy = None
        min_distance = self.range  

        for enemy in Enemy.all_enemies:
            distance = self.find_distance(enemy)
            if distance < self.range and distance < min_distance:
                closest_enemy = enemy
                min_distance = distance  

        if closest_enemy:
            self.target = closest_enemy
        else:
            self.target = None  

    def find_distance(self, enemy):
        distance = math.sqrt((enemy.x - self.x) ** 2 + (enemy.y - self.y) ** 2)
        return distance

    def fire_projectile(self):
        
        if self.target and self.attack_timer >= self.attack_delay:
            self.target_coords = (self.target.x, self.target.y)
            projectile = Projectile(self.x, self.y, self.target_coords, self.dmg)
            print(self.target)
            self.attack_timer = 0

    def update(self):
      
        if not self.target or self.find_distance(self.target) > self.range:
            self.find_target()

        if self.target:
             self.fire_projectile()

        self.attack_timer += 1

       

    def render(self, screen):
        screen.blit(self.sprite, (self.x, self.y))

    def upgrade():
        pass


class Cannon(Tower):
    def __init__(self, x, y, range=100, damage=10, attack_delay=10):
        super().__init__(x, y, range, damage, attack_delay)
        self.sprite = CANNONTOWERSPRITE

class Dart(Tower):
    def __init__(self, x, y, range=100, damage=10, attack_delay=10):
        super().__init__(x, y, range, damage, attack_delay)
        self.sprite = DARTTOWERSPRITE

class Glue(Tower):
    def __init__(self, x, y, range=100, damage=10, attack_delay=10):
       super().__init__(x, y, range, damage, attack_delay)
       self.sprite = GLUETOWERSPRITE

class Boomerang(Tower):
    def __init__(self, x, y, range=100, damage=10, attack_delay=10):
        super().__init__(x, y, range, damage, attack_delay)
        self.sprite = BOOMERANGTOWERSPRITE