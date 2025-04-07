from entities.projectile.cannon_projectile_class import Cannon_Projectile
from entities.tower.base_tower_class import Tower
from entities.sprites import CANNONTOWERSPRITE

class Cannon(Tower):
    cost = 70
    def __init__(self, x, y, range=175, damage=80, attack_delay=100, splash_damage=35, splash_range=1000):
        super().__init__(x, y, range, damage, attack_delay)
        self.sprite = CANNONTOWERSPRITE
        self.splash_damage = splash_damage
        self.splash_range = splash_range
        self.name = 'Cannon Tower'
        self.upgrade_stats = { 1 : { "damage" : 80,
                                    "range" : 175,
                                    "attack delay" : 100,
                                    "cost" : 70
                                },

                                2 : { "damage" : 95,
                                    "range" : 200,
                                    "attack delay" : 95,
                                    "cost" : 50
                                },

                                3 : { "damage" : 120,
                                    "range" : 225,
                                    "attack delay" : 85,
                                    "cost" : 100
                                },
                                }
        
    def fire_projectile(self):
        
        if self.target and self.attack_timer >= self.attack_delay:
            self.target_coords = (self.target.x + (self.target.rect.width / 2), self.target.y + (self.target.rect.height / 2))
            projectile = Cannon_Projectile(self.x + (self.sprite.get_width() / 2), self.y + (self.sprite.get_height()  / 2), self.target_coords, self.damage, self.splash_damage, self.splash_range)
            self.attack_timer = 0