from entities.tower_sprites import *
from entities.enemy import *
from entities.Projectile import *
import math

class Tower():

    all_towers = []

    def __init__(self, x, y):
        self.sprite = None
        self.range = None
        self.dmg = None
        self.cost = None
        self.attack_delay = 10
        self.attack_timer = 0
        self.x = x
        self.y = y
        self.target = None
        self.all_towers.append(self)

    def find_target(self):

        closest_enemy = None
        min_distance = self.range

        for enemy in Enemy.all_enemies:
            distance = math.sqrt((enemy.x - self.x) ** 2 + (enemy.y - self.y) ** 2)
            if distance < min_distance:
                closest_enemy = enemy
                min_distance = distance

        self.target = closest_enemy

    def fire_projectile(self):
        self.attack_timer += 1
        if self.target and self.attack_timer >= self.attack_delay:
            projectile = Projectile(self.x, self.y, self.target, self.dmg)
            self.attack_timer = 0

       

    def render(self, screen):
        screen.blit(self.sprite, (self.x, self.y))

    def upgrade():
        pass


class Cannon(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.sprite = CANNONTOWERSPRITE

class Dart(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.sprite = DARTTOWERSPRITE

class Glue(Tower):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.sprite = GLUETOWERSPRITE

class Boomerang(Tower):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.sprite = BOOMERANGTOWERSPRITE