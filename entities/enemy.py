from GridManager import *

class Enemy():

    all_enemies = []

    def __init__(self) -> None:
        self.all_enemies.append(self)

    def is_dead(self):
        if self.health <= 0:
            self.all_ememies.pop(self)

    def move():
        pass

    def update():
        pass

    def follow_path():
        pass

    def take_damage(self, damage):
        self.health -= damage

    def render():
        pass

class EnemyVariant1(Enemy):
    def __init__(self, x, y, health, damage, speed):
        super().__init__()
        self.x = x
        self.y = y
        self.health = health
        self.damage = damage
        self.speed = speed

        
        