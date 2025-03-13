from tower_sprites import *

class Tower():

    all_towers = []

    def __init__(self, x, y) -> None:
        self.sprite = None
        self.range = None
        self.dmg = None
        self.cost = None
        self.attack_spd = None
        self.x = x
        self.y = y
        self.all_towers.append(self)

    def target_enemy():
        pass

    def render(self, screen):
        screen.blit(self.sprite (self.x, self.y))

    def upgrade():
        pass

    def find_in_range():
        pass

class Cannon(Tower):
    def __init__(self) -> None:
        super().__init__()
        self.sprite = CANNONTOWERSPRITE

class Dart(Tower):
    def __init__(self) -> None:
        super().__init__()
        self.sprite = DARTTOWERSPRITE

class Glue(Tower):
    def __init__(self) -> None:
        super().__init__()
        self.sprite = GLUETOWERSPRITE

class Boomerang(Tower):
    def __init__(self) -> None:
        super().__init__()
        self.sprite = BOOMERANGTOWERSPRITE