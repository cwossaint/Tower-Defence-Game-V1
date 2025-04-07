from entities.projectile.base_projectile_class import *
from constants.global_constants import BLUE

class Boomerang_Projectile(Projectile):
    def __init__(self, x, y, target, damage, size=20, shape="circle", speed=20, color=BLUE):
        super().__init__(x, y, target, damage, size, shape, speed, color)
        self.enemies_hit = []

    def check_collision(self):
            for enemy in Enemy.all_enemies:
                if pygame.Rect.colliderect(self.rect, enemy.rect):
                        if not enemy in self.enemies_hit:
                            self.enemies_hit.append(enemy)
                            enemy.take_damage(self.damage)
