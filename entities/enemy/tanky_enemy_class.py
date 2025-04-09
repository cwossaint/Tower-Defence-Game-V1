from entities.enemy.base_enemy_class import Enemy
from entities.sprites import TANKYENEMYSPRITE

class Tanky_Enemy(Enemy):
    def __init__(self, x, y, directions_list, game_data, wave, health=50, damage=20, speed=3):
        # Initialize the base Enemy class with tanky stats (high health, lower speed)
        super().__init__(x, y, directions_list, game_data, wave, health, damage, speed)

        # Assign the specific sprite for this enemy type
        self.sprite = TANKYENEMYSPRITE

        # Set the value (reward in cash) the player gets when this enemy is defeated
        self.value = 10

        # Define the collision/rendering boundary using the sprite's size and current position
        self.update_rect()

        # Scale the stats according to the current wave for increasing difficulty
        self.scale_stats()
