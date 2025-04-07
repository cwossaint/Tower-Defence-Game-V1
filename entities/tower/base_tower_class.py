from entities.enemy.base_enemy_class import *
import math

class Tower():

    all_towers = []

    def __init__(self, x, y, range=100, damage=1, attack_delay=10):
        self.sprite = None
        self.projectile_type = None
        self.range = range
        self.damage = damage
        self.attack_delay = attack_delay
        self.attack_timer = 0
        self.x = x
        self.y = y
        self.target_coords = None
        self.target = None
        self.level = 1
        self.upgrade_stats = {}
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
        pass

    def update(self):
      
        if not self.target or self.find_distance(self.target) > self.range or self.target.removed == True:

            self.find_target()

        if self.target:
             self.fire_projectile()

        self.attack_timer += 1

       

    def render(self, screen):
        screen.blit(self.sprite, (self.x, self.y))

    def upgrade(self):
        if not self.level + 1 > len(self.upgrade_stats):
            self.level += 1
            upgrade_stats = self.upgrade_stats.get(self.level)
            self.damage = upgrade_stats.get("damage")
            self.range = upgrade_stats.get("range")
            self.attack_delay = upgrade_stats.get("attack delay")

