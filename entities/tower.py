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
    cost = 70
    def __init__(self, x, y, range=100, damage=35, attack_delay=50):
        super().__init__(x, y, range, damage, attack_delay)
        self.sprite = CANNONTOWERSPRITE
        self.projectile_type = "CannonBall"
        self.name = 'Cannon Tower'
        self.upgrade_stats = { 1 : { "damage" : 35,
                                    "range" : 100,
                                    "attack delay" : 50,
                                    "cost" : 70
                                },

                                2 : { "damage" : 45,
                                    "range" : 125,
                                    "attack delay" : 47,
                                    "cost" : 150
                                },

                                3 : { "damage" : 55,
                                    "range" : 175,
                                    "attack delay" : 42,
                                    "cost" : 250
                                },
                                }

class Dart(Tower):
    cost = 25
    def __init__(self, x, y, range=150, damage=9, attack_delay=30):
        super().__init__(x, y, range, damage, attack_delay)
        self.sprite = DARTTOWERSPRITE
        self.projectile_type = "Dart"
        self.name = 'Dart Tower'
        self.upgrade_stats = { 1 : { "damage" : 9,
                                    "range" : 150,
                                    "attack delay" : 30,
                                    "cost" : 25
                                },

                                2 : { "damage" : 12,
                                    "range" : 175,
                                    "attack delay" : 27,
                                    "cost" : 100
                                },

                                3 : { "damage" : 18,
                                    "range" : 250,
                                    "attack delay" : 25,
                                    "cost" : 175
                                },
                                }

class Glue(Tower):
    cost = 25
    def __init__(self, x, y, range=150, damage=3, attack_delay=70):
       super().__init__(x, y, range, damage, attack_delay)
       self.sprite = GLUETOWERSPRITE
       self.projectile_type = "Glue"
       self.name = 'Glue Tower'
       self.upgrade_stats = { 1 : { "damage" : 3,
                                    "range" : 150,
                                    "attack delay" : 70,
                                    "cost" : 25
                                },

                                2 : { "damage" : 4,
                                    "range" : 175,
                                    "attack delay" : 13,
                                    "cost" : 75
                                },

                                3 : { "damage" : 5,
                                    "range" : 250,
                                    "attack delay" : 12,
                                    "cost" : 125
                                },
                                }

class Boomerang(Tower):
    cost = 25
    def __init__(self, x, y, range=250, damage=15, attack_delay=40):
        super().__init__(x, y, range, damage, attack_delay)
        self.sprite = BOOMERANGTOWERSPRITE
        self.projectile_type = "Boomerang"
        self.name = 'Boomerang Tower'
        self.upgrade_stats = { 1 : { "damage" : 15,
                                    "range" : 250,
                                    "attack delay" : 40,
                                    "cost" : 25
                                },

                                2 : { "damage" : 18,
                                    "range" : 300,
                                    "attack delay" : 35,
                                    "cost" : 75
                                },

                                3 : { "damage" : 25,
                                    "range" : 450,
                                    "attack delay" : 31,
                                    "cost" : 225
                                },
                                }
        
class Gatling(Tower):
    cost = 110
    def __init__(self, x, y, range=250, damage=2, attack_delay=5):
        super().__init__(x, y, range, damage, attack_delay)
        self.sprite = GATLINGTOWERSPRITE
        self.projectile_type = "Gatling"
        self.name = 'Gatling Tower'
        self.upgrade_stats = { 1 : { "damage" : 2,
                                    "range" : 250,
                                    "attack delay" : 5,
                                    "cost" : 110
                                },

                                2 : { "damage" : 3,
                                    "range" : 300,
                                    "attack delay" : 5,
                                    "cost" : 80
                                },

                                3 : { "damage" : 5,
                                    "range" : 350,
                                    "attack delay" : 4,
                                    "cost" : 175
                                },
                                }