class Enemy():
    def __init__(self) -> None:
        pass

    def is_dead():
        pass

    def move():
        pass

    def follow_path():
        pass

    def take_damage():
        pass

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

        
        