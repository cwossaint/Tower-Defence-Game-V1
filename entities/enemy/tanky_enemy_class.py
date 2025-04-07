from entities.enemy.base_enemy_class import Enemy
from entities.sprites import TANKYENEMYSPRITE


class Tanky_Enemy(Enemy):
    def __init__(self, x, y, directions_list, game_data, wave, health=50, damage=20, speed=3):
        super().__init__(x, y, directions_list, game_data, wave, health, damage, speed)
        self.sprite = TANKYENEMYSPRITE
        self.value = 10
        self.update_rect()
        self.scale_stats()
        #print("Tanky health" + str(self.health))
        #print("Tanky speed: " + str(self.speed))
        #print("Tanky damage: " + str(self.damage))