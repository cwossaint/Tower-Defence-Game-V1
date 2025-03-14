
class Projectile():

    all_projectiles = []

    def __init__(self, x, y, target, damage) -> None:
        self.x = x
        self.y = y
        self.target = target
        self.sprite = None
        self.damage = damage
        self.all_projectiles.append(self)

    def update(self):
        pass
        
    def destroy(self):
        self.all_projectiles.remove(self)

    def render(self, screen):
        screen.blit(self.sprite, (self.x, self.y))