from entities.enemy.base_enemy_class import Enemy
from entities.sprites import SPEEDYENEMYSPRITE

class Speedy_Enemy(Enemy):
    def __init__(self, x, y, directions_list, game_data, wave, health=15, damage=10, speed=10):
        super().__init__(x, y, directions_list, game_data, wave, health, damage, speed)
        self.sprite = SPEEDYENEMYSPRITE
        self.value = 5
        self.update_rect()
        self.scale_stats()
        #print("Speedy speed: " + str(self.speed))
        #print("Speedy Health: " + str(self.health))
        #print("Speedy damage: " + str(self.damage))
