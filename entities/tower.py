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

    def upgrade(self):
        if not self.level + 1 > len(self.upgrade_stats):
            self.level += 1
            upgrade_stats = self.upgrade_stats.get(self.level)
            self.damage = upgrade_stats.get("damage")
            self.range = upgrade_stats.get("range")
            self.attack_delay = upgrade_stats.get("attack delay")



class Cannon(Tower):
    cost = 10
    def __init__(self, x, y, range=100, damage=1, attack_delay=10):
        super().__init__(x, y, range, damage, attack_delay)
        self.sprite = CANNONTOWERSPRITE
        self.projectile_type = "CannonBall"
        self.name = 'Cannon Tower'
        self.upgrade_stats = { 1 : { "damage" : 10,
                                    "range" : 100,
                                    "attack delay" : 10,
                                    "cost" : 10
                                },

                                2 : { "damage" : 12,
                                    "range" : 125,
                                    "attack delay" : 8,
                                    "cost" : 50
                                },

                                3 : { "damage" : 100,
                                    "range" : 175,
                                    "attack delay" : 1,
                                    "cost" : 50
                                },
                                }

class Dart(Tower):
    cost = 50
    def __init__(self, x, y, range=100, damage=20, attack_delay=10):
        super().__init__(x, y, range, damage, attack_delay)
        self.sprite = DARTTOWERSPRITE
        self.projectile_type = "Dart"
        self.name = 'Dart Tower'
        self.upgrade_stats = { 1 : { "damage" : 20,
                                    "range" : 100,
                                    "attack delay" : 10,
                                    "cost" : 50
                                },

                                2 : { "damage" : 25,
                                    "range" : 175,
                                    "attack delay" : 10,
                                    "cost" : 75
                                },

                                3 : { "damage" : 1,
                                    "range" : 1000,
                                    "attack delay" : 1,
                                    "cost" : 150
                                },
                                }

class Glue(Tower):
    cost = 10
    def __init__(self, x, y, range=100, damage=1, attack_delay=10):
       super().__init__(x, y, range, damage, attack_delay)
       self.sprite = GLUETOWERSPRITE
       self.projectile_type = "Glue"
       self.name = 'Glue Tower'
       self.upgrade_stats = { 1 : { "damage" : 1,
                                    "range" : 100,
                                    "attack delay" : 10,
                                    "cost" : 10
                                },

                                2 : { "damage" : 2,
                                    "range" : 150,
                                    "attack delay" : 5,
                                    "cost" : 45
                                },

                                3 : { "damage" : 5,
                                    "range" : 250,
                                    "attack delay" : 3,
                                    "cost" : 200
                                },
                                }

class Boomerang(Tower):
    cost = 10
    def __init__(self, x, y, range=250, damage=30, attack_delay=15):
        super().__init__(x, y, range, damage, attack_delay)
        self.sprite = BOOMERANGTOWERSPRITE
        self.projectile_type = "Boomerang"
        self.name = 'Boomerang Tower'
        self.upgrade_stats = { 1 : { "damage" : 30,
                                    "range" : 250,
                                    "attack delay" : 15,
                                    "cost" : 10
                                },

                                2 : { "damage" : 34,
                                    "range" : 300,
                                    "attack delay" : 12,
                                    "cost" : 75
                                },

                                3 : { "damage" : 37,
                                    "range" : 450,
                                    "attack delay" : 1,
                                    "cost" : 250
                                },
                                }