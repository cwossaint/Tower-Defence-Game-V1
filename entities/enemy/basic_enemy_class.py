from entities.enemy.base_enemy_class import Enemy
from entities.sprites import BASEENEMYSPRITE

class Basic_Enemy(Enemy):
    def __init__(self, x, y, directions_list, game_data, wave, health=20, damage=10, speed=5):
        super().__init__(x, y, directions_list, game_data, wave, health, damage, speed)
        self.sprite = BASEENEMYSPRITE
        self.update_rect()
        self.value = 2
        self.scale_stats()
        #print("basic health" + str(self.health))
        #print("basci speed: " + str(self.speed))
        #print("basic damage: " + str(self.damage))



        