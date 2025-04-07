from entities.enemy.base_enemy_class import Enemy
from entities.sprites import BOSSENEMYSPRITE

class Boss_Enemy(Enemy):
    def __init__(self, x, y, directions_list, game_data, wave, health=500, damage=100, speed=1):
        super().__init__(x, y, directions_list, game_data, wave, health, damage, speed)
        self.sprite = BOSSENEMYSPRITE
        self.value = 100
        self.update_rect()
        self.scale_stats()
        #print("Boss health" + str(self.health))
        #print("Boss speed: " + str(self.speed))
        #print("Boss damage: " + str(self.damage))

#self.rect = pygame.Rect(self.x, self.y, self.sprite.get_width(), self.sprite.get_height())
        
       # CATaclysm