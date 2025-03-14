
class Projectile():

    all_projectiles = []

    def __init__(self, x, y, rotation) -> None:
        self.x = x
        self.y = y
        self.rotation = rotation
        self.all_projectiles.append(self)

    def update(self):
        
    def destroy(self):
        self.all_projectiles.remove(self)

    def render(self):