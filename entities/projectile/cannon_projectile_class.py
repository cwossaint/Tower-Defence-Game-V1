from entities.projectile.base_projectile_class import *
from constants.global_constants import BLACK

class Cannon_Projectile(Projectile):
    def __init__(self, x, y, target, damage, splash_damage, splash_range, size=50, shape="circle", speed=10, color=BLACK):
        super().__init__(x, y, target, damage, size, shape, speed, color)
        self.damage = damage
        self.splash_damage = splash_damage
        self.splash_range = splash_range

    def find_enemy_in_range(self, x, y):
        enemies_in_range = []
        for enemy in Enemy.all_enemies:
            distance = math.sqrt((enemy.x + enemy.sprite.get_width()//2 - x) ** 2 + (enemy.y + enemy.sprite.get_height()//2 - y) ** 2)
            if distance <= self.splash_range:
                enemies_in_range.append(enemy)
        return enemies_in_range

    def check_collision(self):
        for enemy in Enemy.all_enemies:
            if pygame.Rect.colliderect(self.rect, enemy.rect):
                self.destroy()
                enemy.take_damage(self.damage)
                enemies_in_range = self.find_enemy_in_range(self.x, self.y)
                for enemy in enemies_in_range:
                    enemy.take_damage(self.splash_damage)
