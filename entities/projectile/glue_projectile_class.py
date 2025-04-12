from entities.projectile.base_projectile_class import *
from constants.global_constants import DARK_YELLOW

class Glue_Projectile(Projectile):
    def __init__(self, x, y, target, damage, slow, splash_range, slow_duration, size=35, shape="circle", speed=15, color=DARK_YELLOW):
        # Initialize the base Projectile attributes and additional glue-specific properties
        super().__init__(x, y, target, damage, size, shape, speed, color)
        self.slow = slow  # The amount of slow applied to enemies hit by the projectile
        self.splash_range = splash_range  # The range in which splash effect (slow) applies to enemies
        self.slow_duration = slow_duration  # The duration for which the enemies remain slowed

    def find_enemy_in_range(self, x, y):
        # Find all enemies within the splash range of the glue effect
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
                # Find and apply the slow effect to enemies within splash range
                enemies_in_range = self.find_enemy_in_range(self.x, self.y)
                for enemy in enemies_in_range:
                    enemy.get_slowed(self.slow, self.slow_duration)  # Apply the slow effect
                self.destroy()  # Destroy the projectile after it has applied its effects
                break
