from entities.projectile.base_projectile_class import *

class Basic_Projectile(Projectile):
    def __init__(self, x, y, target, damage, size=20, shape="circle", speed=20, color=RED):
        # Initialize the Basic_Projectile by calling the base Projectile class constructor
        super().__init__(x, y, target, damage, size, shape, speed, color)
