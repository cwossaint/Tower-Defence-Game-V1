from entities.projectile.base_projectile_class import *
from constants.global_constants import DARK_YELLOW

class Glue_Projectile(Projectile):
    def __init__(self, x, y, target, damage, slow, splash_range, slow_duration, size=35, shape="circle", speed=15, color=DARK_YELLOW):
        super().__init__(x, y, target, damage, size, shape, speed, color)
        self.slow = slow
        self.splash_range = splash_range
        self.slow_duration = slow_duration

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
                enemies_in_range = self.find_enemy_in_range(self.x, self.y)
                for enemy in enemies_in_range:
                    enemy.get_slowed(self.slow, self.slow_duration)
                self.destroy()
                break