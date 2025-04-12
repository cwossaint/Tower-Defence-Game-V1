from entities.projectile.base_projectile_class import *
from constants.global_constants import BLACK

class Cannon_Projectile(Projectile):
    def __init__(self, x, y, target, damage, splash_damage, splash_range, size=50, shape="circle", speed=10, color=BLACK):
        # Initialize the base Projectile attributes and additional splash damage and range
        super().__init__(x, y, target, damage, size, shape, speed, color)
        self.damage = damage  # Direct damage to the first enemy hit
        self.splash_damage = splash_damage  # Splash damage to enemies within range of impact
        self.splash_range = splash_range  # Range within which enemies receive splash damage

    def find_enemy_in_range(self, x, y):
        # Find all enemies within the splash range of the explosion
        enemies_in_range = []
        for enemy in Enemy.all_enemies:
            # Calculate the distance between the explosion and the enemy
            distance = math.sqrt((enemy.x + enemy.sprite.get_width()//2 - x) ** 2 + (enemy.y + enemy.sprite.get_height()//2 - y) ** 2)
            # If the enemy is within the splash range, add it to the list
            if distance <= self.splash_range:
                enemies_in_range.append(enemy)
        return enemies_in_range

    def check_collision(self):
        # Check for collision with each enemy
        for enemy in Enemy.all_enemies:
            if pygame.Rect.colliderect(self.rect, enemy.rect):  # If the projectile hits an enemy
                enemy.take_damage(self.damage)  # Apply direct damage
                # Find and apply splash damage to enemies within range
                enemies_in_range = self.find_enemy_in_range(self.x, self.y)
                for enemy in enemies_in_range:
                    enemy.take_damage(self.splash_damage)
                self.destroy()  # Destroy the projectile after impact
                break
