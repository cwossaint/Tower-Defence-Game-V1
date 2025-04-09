from entities.enemy.base_enemy_class import Enemy
from entities.sprites import SPEEDYENEMYSPRITE

class Speedy_Enemy(Enemy):
    def __init__(self, x, y, directions_list, game_data, wave, health=15, damage=10, speed=10):
        # Initialize the base Enemy class with default stats for a speedy enemy
        super().__init__(x, y, directions_list, game_data, wave, health, damage, speed)

        # Set the sprite for this enemy type
        self.sprite = SPEEDYENEMYSPRITE

        # Set the cash reward for defeating this enemy
        self.value = 5

        # Create the rectangular boundary used for collisions and rendering
        self.update_rect()

        # Scale the enemy's stats based on the current wave
        self.scale_stats()
