from entities.tower_sprites import *
from entities.enemy import *
from entities.Projectile import *
import math

class Tower():

    all_towers = []

    def __init__(self, x, y, range=100, damage=1, attack_delay=10):
        self.sprite = None
        self.projectile_type = None
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

    def remove_tower(self):
        if self in Tower.all_towers:
            Tower.all_towers.remove(self)

    def fire_projectile(self):
        
        if self.target and self.attack_timer >= self.attack_delay:
            self.target_coords = (self.target.x + (self.target.rect.width / 2), self.target.y + (self.target.rect.height / 2))
            projectile = Projectile(self.x + (self.sprite.get_width() / 2), self.y + (self.sprite.get_height()  / 2), self.target_coords, self.damage, self.projectile_type)
            self.attack_timer = 0

    def update(self):
      
        if not self.target or self.find_distance(self.target) > self.range or self.target.removed == True:

            self.find_target()

        if self.target:
             self.fire_projectile()

        self.attack_timer += 1

       

    def render(self, screen):
        screen.blit(self.sprite, (self.x, self.y))

    def upgrade():
        pass


class Cannon(Tower):
    cost = 10
    def __init__(self, x, y, range=100, damage=1, attack_delay=10):
        super().__init__(x, y, range, damage, attack_delay)
        self.sprite = CANNONTOWERSPRITE
        self.projectile_type = "CannonBall"

class Dart(Tower):
    cost = 50
    def __init__(self, x, y, range=1000, damage=20, attack_delay=-5):
        super().__init__(x, y, range, damage, attack_delay)
        self.sprite = DARTTOWERSPRITE
        self.projectile_type = "Dart"

class Glue(Tower):
    cost = 10
    def __init__(self, x, y, range=100, damage=1, attack_delay=10):
       super().__init__(x, y, range, damage, attack_delay)
       self.sprite = GLUETOWERSPRITE
       self.projectile_type = "Glue"

class Boomerang(Tower):
    cost = 10
    def __init__(self, x, y, range=100, damage=1, attack_delay=10):
        super().__init__(x, y, range, damage, attack_delay)
        self.sprite = BOOMERANGTOWERSPRITE
        self.projectile_type = "Boomerang"