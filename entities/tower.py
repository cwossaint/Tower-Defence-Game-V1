from tower_sprites import *

class Tower():

    all_towers = []

    def __init__(self) -> None:
        self.sprite = None
        self.range = None
        self.dmg = None
        self.cost = None
        self.attack_spd = None
        self.x = None
        self.y = None
        self.all_towers.append(self)

    def target_enemy():
        pass

    def render(self, screen):
        screen.blit(self.sprite (self.x, self.y))

    def upgrade():
        pass

    def find_in_range():
        pass

    