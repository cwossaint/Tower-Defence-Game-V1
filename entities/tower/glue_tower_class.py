from entities.tower.base_tower_class import Tower
from entities.projectile.glue_projectile_class import Glue_Projectile
from entities.sprites import GLUETOWERSPRITE

class Glue(Tower):
    cost = 25
    def __init__(self, x, y, range=150, damage=0, attack_delay=70, slow=0.5, splash_range=80):
       super().__init__(x, y, range, damage, attack_delay)
       self.sprite = GLUETOWERSPRITE
       self.splash_range = splash_range
       self.slow = slow
       self.name = 'Glue Tower'
       self.upgrade_stats = { 1 : { "damage" : 3,
                                    "range" : 150,
                                    "attack delay" : 70,
                                    "cost" : 25
                                },

                                2 : { "damage" : 4,
                                    "range" : 175,
                                    "attack delay" : 13,
                                    "cost" : 15
                                },

                                3 : { "damage" : 5,
                                    "range" : 250,
                                    "attack delay" : 12,
                                    "cost" : 35
                                },
                                }
       
    def fire_projectile(self):
        
        if self.target and self.attack_timer >= self.attack_delay:
            self.target_coords = (self.target.x + (self.target.rect.width / 2), self.target.y + (self.target.rect.height / 2))
            projectile = Glue_Projectile(self.x + (self.sprite.get_width() / 2), self.y + (self.sprite.get_height()  / 2), self.target_coords, self.damage, self.slow, self.splash_range)
            self.attack_timer = 0