from entities.projectile.basic_projectile_class import Basic_Projectile
from entities.tower.base_tower_class import Tower
from entities.sprites import GATLINGTOWERSPRITE

class Gatling(Tower):
    cost = 110
    def __init__(self, x, y, range=250, damage=2, attack_delay=5):
        super().__init__(x, y, range, damage, attack_delay)
        self.sprite = GATLINGTOWERSPRITE
        self.find_centre()
        self.projectile_type = "Gatling"
        self.name = 'Gatling Tower'
        self.upgrade_stats = { 1 : { "damage" : 2,
                                    "range" : 250,
                                    "attack delay" : 5,
                                    "cost" : 110
                                },

                                2 : { "damage" : 2,
                                    "range" : 300,
                                    "attack delay" : 4.75,
                                    "cost" : 55
                                },

                                3 : { "damage" : 2.4,
                                    "range" : 350,
                                    "attack delay" : 4,
                                    "cost" : 95
                                },
                                }
        
    def fire_projectile(self):
        if self.target and self.attack_timer >= self.attack_delay:
            self.target_coords = (self.target.x + (self.target.rect.width / 2), self.target.y + (self.target.rect.height / 2))
            projectile = Basic_Projectile(self.centrex, self.centrey, self.target_coords, self.damage)
            self.attack_timer = 0