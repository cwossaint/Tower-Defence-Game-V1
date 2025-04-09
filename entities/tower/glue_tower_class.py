from entities.tower.base_tower_class import Tower
from entities.projectile.glue_projectile_class import Glue_Projectile
from entities.sprites import GLUETOWERSPRITE

class Glue(Tower):
    cost = 25
    def __init__(self, x, y, range=150, damage=0, attack_delay=70, slow=0.5, splash_range=80, slow_duration=180):
       super().__init__(x, y, range, damage, attack_delay)
       self.sprite = GLUETOWERSPRITE
       self.find_centre()
       self.splash_range = splash_range
       self.slow = slow
       self.slow_duration = slow_duration
       self.name = 'Glue Tower'
       self.upgrade_stats = { 1 : { "slow" : 0.5,
                                    "range" : 150,
                                    "attack delay" : 70,
                                    "slow duration" : 180,
                                    "splash range" : 80,
                                    "cost" : 25
                                },

                                2 : { "slow" : 0.6,
                                    "range" : 175,
                                    "attack delay" : 60,
                                    "slow duration" : 250,
                                    "splash range" : 100,
                                    "cost" : 30
                                },

                                3 : { "slow" : 0.8,
                                    "range" : 250,
                                    "attack delay" : 45,
                                    "slow duration" : 300,
                                    "splash range" : 80,
                                    "cost" : 55
                                },
                                }
       
    def fire_projectile(self):
        
        if self.target and self.attack_timer >= self.attack_delay:
            self.target_coords = (self.target.x + (self.target.rect.width / 2), self.target.y + (self.target.rect.height / 2))
            projectile = Glue_Projectile(self.centrex, self.centrey, self.target_coords, self.damage, self.slow, self.splash_range, self.slow_duration)
            self.attack_timer = 0

    def upgrade(self):
        if not self.level + 1 > len(self.upgrade_stats):
            self.level += 1
            upgrade_stats = self.upgrade_stats.get(self.level)
            self.slow = upgrade_stats.get("slow")
            self.range = upgrade_stats.get("range")
            self.attack_delay = upgrade_stats.get("attack delay")
            self.slow_duration = upgrade_stats.get("slow duration")
            self.splash_range = upgrade_stats.get("splash range")