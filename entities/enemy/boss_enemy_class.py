from entities.enemy.base_enemy_class import Enemy
from entities.sprites import BOSSENEMYSPRITE

#CATacylsm
class Boss_Enemy(Enemy):
    def __init__(self, x, y, directions_list, game_data, wave, health=500, damage=100, speed=1):
        # Initialize the base Enemy class with given or default boss stats
        super().__init__(x, y, directions_list, game_data, wave, health, damage, speed)

        # Assign the boss enemy sprite
        self.sprite = BOSSENEMYSPRITE

        # Set the value (cash reward) for defeating the boss
        self.value = 100

        # Update the rectangle for collision/rendering
        self.update_rect()

        # Apply stat scaling based on the current wave
        self.scale_stats()
