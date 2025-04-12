from entities.projectile.base_projectile_class import *
from constants.global_constants import BLUE

class Boomerang_Projectile(Projectile):
    def __init__(self, x, y, target, damage, pierce, size=20, shape="circle", speed=20, color=BLUE):
        # Initialize the base Projectile attributes
        super().__init__(x, y, target, damage, size, shape, speed, color)
        self.enemies_hit = []  # Keep track of enemies already hit to avoid hitting the same one again
        self.pierce = pierce  # Number of enemies the projectile can hit before being destroyed

    def check_collision(self):
        # Check for collision with each enemy in the game
        for enemy in Enemy.all_enemies:
            if pygame.Rect.colliderect(self.rect, enemy.rect):
                if not enemy in self.enemies_hit:  # Only hit enemies that haven't been hit yet
                    self.pierce -= 1  # Decrease pierce count
                    self.enemies_hit.append(enemy)  # Add enemy to hit list
                    enemy.take_damage(self.damage)  # Apply damage to the enemy
                    if self.pierce <= 0:
                        self.destroy()  # Destroy projectile if it can't pierce anymore
                        break
