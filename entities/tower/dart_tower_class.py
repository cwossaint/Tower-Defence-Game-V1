from entities.projectile.basic_projectile_class import Basic_Projectile
from entities.tower.base_tower_class import Tower
from entities.sprites import DARTTOWERSPRITE


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
                                    "cost" : 25
                                },

                                3 : { "damage" : 18,
                                    "range" : 250,
                                    "attack delay" : 25,
                                    "cost" : 45
                                },

                                4 : { "damage" : 25,
                                    "range" : 500,
                                    "attack delay" : 1,
                                    "cost" : 1000
                                },
                                }
    def fire_projectile(self):
        if self.target and self.attack_timer >= self.attack_delay:
            self.target_coords = (self.target.x + (self.target.rect.width / 2), self.target.y + (self.target.rect.height / 2))
            projectile = Basic_Projectile(self.x + (self.sprite.get_width() / 2), self.y + (self.sprite.get_height()  / 2), self.target_coords, self.damage)
            self.attack_timer = 0
