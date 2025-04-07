from entities.projectile.boomerang_projectile_class import Boomerang_Projectile
from entities.tower.base_tower_class import Tower
from entities.sprites import BOOMERANGTOWERSPRITE

class Boomerang(Tower):
    cost = 25
    def __init__(self, x, y, range=250, damage=7, attack_delay=50, pierce=5):
        super().__init__(x, y, range, damage, attack_delay)
        self.sprite = BOOMERANGTOWERSPRITE
        self.pierce = pierce
        self.name = 'Boomerang Tower'
        self.upgrade_stats = { 1 : { "damage" : 7,
                                    "range" : 250,
                                    "attack delay" : 50,
                                    "pierce" : 5,
                                    "cost" : 25
                                },

                                2 : { "damage" : 10,
                                    "range" : 300,
                                    "attack delay" : 45,
                                    "pierce" : 7,
                                    "cost" : 35
                                },

                                3 : { "damage" : 15,
                                    "range" : 450,
                                    "attack delay" : 35,
                                    "pierce" : 15,
                                    "cost" : 125
                                },
                                }
        
    def fire_projectile(self):
        
        if self.target and self.attack_timer >= self.attack_delay:
            self.target_coords = (self.target.x + (self.target.rect.width / 2), self.target.y + (self.target.rect.height / 2))
            projectile = Boomerang_Projectile(self.x + (self.sprite.get_width() / 2), self.y + (self.sprite.get_height() / 2), self.target_coords, self.damage, self.pierce)
            self.attack_timer = 0

    def upgrade(self):
        if not self.level + 1 > len(self.upgrade_stats):
            self.level += 1
            upgrade_stats = self.upgrade_stats.get(self.level)
            self.damage = upgrade_stats.get("damage")
            self.range = upgrade_stats.get("range")
            self.attack_delay = upgrade_stats.get("attack delay")
            self.pierce = upgrade_stats.get("pierce")
