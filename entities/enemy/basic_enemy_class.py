from entities.enemy.base_enemy_class import Enemy
from entities.sprites import BASEENEMYSPRITE

class Basic_Enemy(Enemy):
    def __init__(self, x, y, directions_list, game_data, wave, health=20, damage=10, speed=5):
        # Initialize the base Enemy class with default or given stats
        super().__init__(x, y, directions_list, game_data, wave, health, damage, speed)

        # Assign the enemy's sprite
        self.sprite = BASEENEMYSPRITE

        # Create or update the enemy's rect for collision and rendering
        self.update_rect()

        # Set the cash value awarded when this enemy is destroyed
        self.value = 2

        # Apply wave-based scaling to this enemy's stats
        self.scale_stats()
